from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse,urlencode



import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden


from  authapp.models import UserProfile

def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about','personal','photo_200')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['sex']:
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['about']:
        user.userprofile.about_me = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        user.userprofile.age_form = bdate
        if age < 18:
            user.delete()

    if data['personal']['langs']:
       user.userprofile.langs =  data['personal']['langs'][0] if len(data['personal']['langs'][0])>0 else 'EN'

    # if data['photo_200']:
    #     user.avatar =