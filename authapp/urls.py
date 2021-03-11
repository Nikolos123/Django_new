from django.urls import path
from authapp.views import login, register, profile, new_logout

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('new-logout/', new_logout, name='new_logout'),
]
