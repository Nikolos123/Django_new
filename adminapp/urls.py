from django.urls import path
# from adminapp.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete
from adminapp.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView,ProductsListView,ProductsUpdateView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-creat/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),

    # Products
    path('products/', ProductsListView.as_view(), name='admin_products'),
    path('products-update/<int:pk>/', ProductsUpdateView.as_view(), name='admin_products_update'),
]
