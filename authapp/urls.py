from django.urls import path

# from authapp.views import login, register, profile, new_logout
from authapp.views import LoginListView, ProfileFormView, Logout,RegisterListView,privacy_policy

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('', Logout.as_view(), name='new_logout'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('verify/<str:email>/<str:activation_key>/', RegisterListView.verify, name='verify'),

]
