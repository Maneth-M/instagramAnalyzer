from django.shortcuts import render
from projects.models import Project
from accounts.models import Media
from home.views import cl
from datetime import datetime, timedelta
from urllib.parse import quote
from django.db.models import Max



def media (request):
    project = request.GET.get('project', "")
    sort = request.GET.get("sort", "")
    minDate = request.GET.get("minDate", "")
    maxDate = request.GET.get("maxDate", "")
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
                        analyze = {
                            f"{datetime.now()}":
                                {
                                    "likes": result.like_count,
                                    "comments": result.comment_count,
                                    "views": result.view_count,
                                }
                        }
                        Media(
                            mediaId=result.id,
                            account=account,
                            source= source,
                            type=mType,
                            likes=result.like_count,
                            comments=result.comment_count,
                            views=result.view_count,
                            analyze=analyze,
                            caption={result.caption_text},
                            hashtags=hashtags,
                            resources=resources,
                            datePosted=result.taken_at
                        ).save()

        if sort == "" or sort == "L":
            medias = Media.objects.filter(account__in=accounts).all().annotate(Max("likes")).order_by('-likes__max')
        elif sort == "C":
            medias = Media.objects.filter(account__in=accounts).all().annotate(Max("comments")).order_by('-comments__max')
        else:
            medias = Media.objects.filter(account__in=accounts).all().annotate(Max("views")).order_by('-views__max')

        tod = datetime.now()
        d = timedelta(days = 45)
        a = tod - d
        a = a.strftime("%Y-%m-%d")



        if minDate and maxDate:
            medias = medias.filter(datePosted__range=[str(minDate), str(maxDate)])

        minDate = {
            'min': a,
            'max': datetime.now().strftime("%Y-%m-%d")
        }

        return render(
            request,
            "analyze/analyze.html",
            {
                'medias': medias,
                'project': project,
                'dates': minDate,
                'sort': sort
            }
        )