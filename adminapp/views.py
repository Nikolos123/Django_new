from re import error

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm


def index(request):
    return render(request, 'index.html')


# READ
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'admin-users-read.html', context)


# CREAT
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
def admin_users_update(request):
    return render(request, 'admin-users-update-delete.html')


# DELETE
def admin_users_delete(request):
    pass
