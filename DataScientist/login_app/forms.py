
from django import forms
from django.contrib.auth.models import User
from login_app.models import UserProfileInfo



#creating forms for models

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))        
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)



