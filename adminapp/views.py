from re import error

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForim
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser,login_url='/')
def index(request):
    return render(request, 'index.html')


# READ
@user_passes_test(lambda u: u.is_superuser,login_url='/')
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'admin-users-read.html', context)


# CREAT
@user_passes_test(lambda u: u.is_superuser,login_url='/')
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        else:
            print(error)
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'admin-users-creat.html', context)


# UPDATE
@user_passes_test(lambda u: u.is_superuser,login_url='/')
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForim(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForim(instance=user)

    context = {
        'title': 'GeekShop - Профиль',
        'form': form,
        'user':user,
    }

    return render(request, 'admin-users-update-delete.html', context)


# DELETE
@user_passes_test(lambda u: u.is_superuser,login_url='/')
def admin_users_delete(request,user_id):
    user = User.objects.get(id=user_id)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))

