from authapp.forms import UserRegisterForm,UserProfileForm
from authapp.models import User
from django import forms
from mainapp.forms import ProductProfileForm,ProductCategory


class UserAdminRegistrationForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'

class UserAdminProfileForim(UserProfileForm):


    def __init__(self,*args,**kwargs):
        super(UserAdminProfileForim, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False

class ProductAdminProfileForm(ProductProfileForm):


    def __init__(self,*args,**kwargs):
        super(ProductAdminProfileForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['readonly'] = False
        # self.fields['email'].widget.attrs['readonly'] = False

class CategoryAdminProfileForm(ProductCategory):

    def __init__(self,*args,**kwargs):
        super(CategoryAdminProfileForm, self).__init__(*args,**kwargs)