from instagrapi import Client

cl = Client()
cl.login('butterbunny23', '123AgunamD')
result = cl.user_info_by_username('instagram').dict()

print(result)


{
    'pk': '25025320',
    'username': 'instagram',
    'full_name': 'Instagram',
    'is_private': False,
    'profile_pic_url': HttpUrl('https://instagram.fcmb11-1.fna.fbcdn.net/v/t51.2885-19/203019087_3969530746500786_7930596639916235962_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fcmb11-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=uDzQ1eq4ZmIAX9qqQB9&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT81MczaNcqC5MASrbfsrsxVGHpqlKGNL91T4i5w37CTPQ&oe=622F2702&_nc_sid=7bff83', scheme='https', host='instagram.fcmb11-1.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-19/203019087_3969530746500786_7930596639916235962_n.jpg', query='stp=dst-jpg_s150x150&_nc_ht=instagram.fcmb11-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=uDzQ1eq4ZmIAX9qqQB9&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT81MczaNcqC5MASrbfsrsxVGHpqlKGNL91T4i5w37CTPQ&oe=622F2702&_nc_sid=7bff83'),
    'profile_pic_url_hd': HttpUrl('https://instagram.fcmb11-1.fna.fbcdn.net/v/t51.2885-19/203019087_3969530746500786_7930596639916235962_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fcmb11-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=uDzQ1eq4ZmIAX9qqQB9&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT9MSKdQLAG_7bzlOCXxyLiHCLm3q1r5svvOBFoEhFRvAg&oe=622F2702&_nc_sid=7bff83', scheme='https', host='instagram.fcmb11-1.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-19/203019087_3969530746500786_7930596639916235962_n.jpg', query='stp=dst-jpg_s320x320&_nc_ht=instagram.fcmb11-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=uDzQ1eq4ZmIAX9qqQB9&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT9MSKdQLAG_7bzlOCXxyLiHCLm3q1r5svvOBFoEhFRvAg&oe=622F2702&_nc_sid=7bff83'),
    'is_verified': True,
    'media_count': 7077,
    'follower_count': 478726381,
    'following_count': 108,
    'biography': '#YoursToMake',
    'external_url': 'http://help.instagram.com/',
    'is_business': False,
    'public_email': None,
    'contact_phone_number': None,
    'business_contact_method': 'UNKNOWN',
    'business_category_name': None,
    'category_name': 'Digital creator'
}


