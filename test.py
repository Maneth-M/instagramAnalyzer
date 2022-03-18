from instagrapi import Client

cl = Client()
cl.login('butterbunny23', '123AgunamD')
result = cl.user_info_by_username('instagram')
print(result)


# {
#     'pk': '25025320',
#     'username': 'instagram',
#     'full_name': 'Instagram',
#     'is_private': False,
#     'profile_pic_url': HttpUrl('https://instagram.fcmb11-1.fna.fbcdn.net/v/t51.2885-19/203019087_3969530746500786_7930596639916235962_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fcmb11-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=uDzQ1eq4ZmIAX9qqQB9&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT81MczaNcqC5MASrbfsrsxVGHpqlKGNL91T4i5w37CTPQ&oe=622F2702&_nc_sid=7bff83', scheme='https', host='instagram.fcmb11-1.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-19/203019087_3969530746500786_7930596639916235962_n.jpg', query='stp=dst-jpg_s150x150&_nc_ht=instagram.fcmb11-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=uDzQ1eq4ZmIAX9qqQB9&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT81MczaNcqC5MASrbfsrsxVGHpqlKGNL91T4i5w37CTPQ&oe=622F2702&_nc_sid=7bff83'),
#     'profile_pic_url_hd': HttpUrl('https://instagram.fcmb11-1.fna.fbcdn.net/v/t51.2885-19/203019087_3969530746500786_7930596639916235962_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fcmb11-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=uDzQ1eq4ZmIAX9qqQB9&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT9MSKdQLAG_7bzlOCXxyLiHCLm3q1r5svvOBFoEhFRvAg&oe=622F2702&_nc_sid=7bff83', scheme='https', host='instagram.fcmb11-1.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-19/203019087_3969530746500786_7930596639916235962_n.jpg', query='stp=dst-jpg_s320x320&_nc_ht=instagram.fcmb11-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=uDzQ1eq4ZmIAX9qqQB9&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT9MSKdQLAG_7bzlOCXxyLiHCLm3q1r5svvOBFoEhFRvAg&oe=622F2702&_nc_sid=7bff83'),
#     'is_verified': True,
#     'media_count': 7077,
#     'follower_count': 478726381,
#     'following_count': 108,
#     'biography': '#YoursToMake',
#     'external_url': 'http://help.instagram.com/',
#     'is_business': False,
#     'public_email': None,
#     'contact_phone_number': None,
#     'business_contact_method': 'UNKNOWN',
#     'business_category_name': None,
#     'category_name': 'Digital creator'
# }
#
#

# [
#     Media(pk='2795369304666013992',
#           id='2795369304666013992_25025320',
#           code='CbLJZJ0pgEo',
#           taken_at=datetime.datetime(2022, 3, 16, 18, 6, 50, tzinfo=datetime.timezone.utc),
#           media_type=8,
#           product_type='',
#           thumbnail_url=None,
#           location=None,
#           user=UserShort(
#               pk='25025320',
#               username='instagram',
#               full_name='',
#               profile_pic_url=None,
#               profile_pic_url_hd=None,
#               is_private=None,
#               stories=[]),
#           comment_count=10072,
#           like_count=344888,
#           has_liked=None,
#           caption_text='“My visual language is like a series of poems that float in my universe.” —Jewel Yang (@a1jewel0310)\n\nJewel combines inspiration from Chinese traditional art — specifically her Kam minority cultural heritage — and her background in bio-textiles to create her “mysterious, organic, dreamy, ethnic-futurist” art.\n\n“My current style was established after I fully embraced my own ethnic culture and started to create similar designs. I look at vessels and weapons from ancient China a lot. I like imagining what the craftsmen back then were thinking and feeling while making those items. I am hugely inspired by the warring states era of Chinese history for its boldness and vividness.”\n\nJewel’s most recent work is an evolution of her distinctive MUA looks to three-dimensional masks. “I was inspired by Chinese traditional shadow play. It is an art form that uses cattle skin as paper. I wanted to create portable makeup looks and have the same mechanism as shadow play characters. Because I focus on bio-textile and natural materials, I created masks using bioplastic.\n\nI want to make Kam minority and Chinese culture sustainable and futuristic. I am also challenging social taboos — because I think behind the superficial and sugar-coated world humans created, the truth underneath is the only path to people’s hearts.”\n\nPhotos by @a1jewel0310',
#           accessibility_caption=None,
#           usertags=[
#               Usertag(
#                   user=UserShort(pk='5960261669', username='a1jewel0310', full_name='', profile_pic_url=None, profile_pic_url_hd=None, is_private=None, stories=[]),
#                   x=0.5658119397, y=0.8538461538000001)],
#           video_url=None,
#           view_count=0,
#           video_duration=0.0,
#           title='',
#           resources=[
#               Resource(
#                   pk='2795369300907972575',
#                   video_url=None,
#                   thumbnail_url=HttpUrl('https://instagram.fcmb4-2.fna.fbcdn.net/v/t51.2885-15/275847440_158328723287736_1639776782245302921_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fcmb4-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=mMH9xxmaQRAAX-fFFpy&edm=APU89FABAAAA&ccb=7-4&oh=00_AT9Pk2AUIM-cRgH2o8Lru7REnGHB6UQKZv7twvJjorTqiQ&oe=623A40AB&_nc_sid=86f79a', scheme='https', host='instagram.fcmb4-2.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-15/275847440_158328723287736_1639776782245302921_n.jpg', query='stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fcmb4-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=mMH9xxmaQRAAX-fFFpy&edm=APU89FABAAAA&ccb=7-4&oh=00_AT9Pk2AUIM-cRgH2o8Lru7REnGHB6UQKZv7twvJjorTqiQ&oe=623A40AB&_nc_sid=86f79a'),
#                   media_type=1),
#               Resource(
#                   pk='2795369300891066830',
#                   video_url=None,
#                   thumbnail_url=HttpUrl('https://instagram.fcmb4-2.fna.fbcdn.net/v/t51.2885-15/275863225_1317744555367916_6242427947659622262_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fcmb4-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=v1SmNI5tAYsAX-9CfgZ&edm=APU89FABAAAA&ccb=7-4&oh=00_AT9vpnlK5O5wQ-P02-I9TUj6wWOMVY67_znpIB4QVXI1dA&oe=623A7AC1&_nc_sid=86f79a', scheme='https', host='instagram.fcmb4-2.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-15/275863225_1317744555367916_6242427947659622262_n.jpg', query='stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fcmb4-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=v1SmNI5tAYsAX-9CfgZ&edm=APU89FABAAAA&ccb=7-4&oh=00_AT9vpnlK5O5wQ-P02-I9TUj6wWOMVY67_znpIB4QVXI1dA&oe=623A7AC1&_nc_sid=86f79a'),
#                   media_type=1),
#               Resource(pk='2795369300874377165', video_url=None, thumbnail_url=HttpUrl('https://instagram.fcmb4-2.fna.fbcdn.net/v/t51.2885-15/275811419_147895214379236_3938912719331903703_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fcmb4-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=884f8q786ikAX87H-XD&edm=APU89FABAAAA&ccb=7-4&oh=00_AT-hZBHl0FJ80UnStPX0jynUIYqSQR_1IP9nFSqYfa7oNg&oe=623AA607&_nc_sid=86f79a', scheme='https', host='instagram.fcmb4-2.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-15/275811419_147895214379236_3938912719331903703_n.jpg', query='stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fcmb4-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=884f8q786ikAX87H-XD&edm=APU89FABAAAA&ccb=7-4&oh=00_AT-hZBHl0FJ80UnStPX0jynUIYqSQR_1IP9nFSqYfa7oNg&oe=623AA607&_nc_sid=86f79a'), media_type=1)],
#           clips_metadata={})]


