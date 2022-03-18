from django.shortcuts import render
from projects.models import Project
from accounts.models import Media
# from home.views import cl
from datetime import datetime




def media (request):
    project = request.GET.get('project', "")
    if project:
        project = Project.objects.filter(projectId=project).first()
        accounts = project.projectAccounts.all()
        for account in accounts:
            results = cl.user_medias(account.accountId,10)
            for result in results:
                if not (datetime.now()-result.taken_at.replace(tzinfo=None)).days >= 45:
                    mType = ""
                    resources = {}
                    if result.media_type == 1:
                        mType = 'photo'
                    elif result.media_type == 8:
                        mType = 'album'
                        for resource in result.resources:
                            resources[resource.pk] = {
                                'type': resource.media_type,
                            }
                    elif result.media_type == 2:
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
                        type=mType,
                        likes={f'{datetime.now()}': result.like_count},
                        views={f'{datetime.now()}': result.view_count},
                        comments={f'{datetime.now()}': result.comment_count},
                        caption={result.caption_text},
                        hashtags=hashtags,
                        resources=resources,
                        datePosted=result.taken_at
                    ).save()