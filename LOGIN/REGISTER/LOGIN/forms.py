from django import forms
from django.contrib.auth.models import User
from LOGIN.models import UserProfileInfo,Company_Info

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class Company_Info_Form(forms.ModelForm):
    class Meta():
        model = Company_Info
        fields = '__all__'
