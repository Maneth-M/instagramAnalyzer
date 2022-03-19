from django.shortcuts import render
from projects.models import Project
from accounts.models import Media
from home.views import cl
from datetime import datetime
from urllib.parse import quote
from django.db.models import Max



def media (request):
    project = request.GET.get('project', "")
    sort = request.GET.get("sort", "")
    if project:
        project = Project.objects.filter(projectId=project).first()
        accounts = project.projectAccounts.all()
        for account in accounts:
            results = cl.user_medias(account.accountId,10)
            for result in results:
                if not (datetime.now()-result.taken_at.replace(tzinfo=None)).days >= 45:
                    if not Media.objects.filter(mediaId=result.id).exists():
                        mType = ""
                        resources = {}
                        source = " "
                        if result.media_type == 1:
                            mType = 'photo'
                            source = quote(result.thumbnail_url)
                        elif result.media_type == 8:
                            mType = 'album'
                            for resource in result.resources:
                                if resource.thumbnail_url:
                                    mSource = quote(resource.thumbnail_url)
                                else:
                                    mSource = quote(resource.video_url)
                                resources[resource.pk] = {
                                    'type': resource.media_type,
                                    'source': mSource
                                }
                        elif result.media_type == 2:
                            source = quote(result.video_url)

                            if result.product_type == "feed":
                                mType = 'video'
                            elif result.product_type == "igtv":
                                mType = 'igtm'
                            elif result.product_type == "clips":
                                mType = 'reel'

                        hashtags = " "
                        for txt in result.caption_text.split():
                            if txt[0] == "#":
                                hashtags = f"{hashtags}{txt} "

                        Media(
                            mediaId=result.id,
                            account=account,
                            source= source,
                            type=mType,
                            rLikes=result.like_count,
                            rComments=result.comment_count,
                            rViews=result.view_count,
                            likes={f'{datetime.now()}': result.like_count},
                            views={f'{datetime.now()}': result.view_count},
                            comments={f'{datetime.now()}': result.comment_count},
                            caption={result.caption_text},
                            hashtags=hashtags,
                            resources=resources,
                            datePosted=result.taken_at
                        ).save()

        if sort == "" or sort == "L":
            medias = Media.objects.filter(account__in=accounts).all().annotate(Max("rLikes")).order_by('-rLikes__max')
        elif sort == "C":
            medias = Media.objects.filter(account__in=accounts).all().annotate(Max("rComments")).order_by('-rComments__max')
        else:
            medias = Media.objects.filter(account__in=accounts).all().annotate(Max("rViews")).order_by('-rViews__max')
        return render(
            request,
            "analyze/analyze.html",
            {
                'medias': medias,
                'project': project
            }
        )