from django.forms import ModelForm
from django import forms
from .models import *


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = MyUser

        fields = '__all__'

        widgets = {'image': forms.FileInput(attrs={'onchange': 'ChangeImage(this)', 'hidden': ''}),
                   'username': forms.TextInput(attrs={'placeholder': 'Логин'}),
                   'password': forms.PasswordInput(attrs={'placeholder': ' Пароль'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Имя'}),
                   'last_name': forms.TextInput(attrs={'placeholder': ' Фамилия'}),
                   'fathername': forms.TextInput(attrs={'placeholder': ' Отчество'}),
                   'email': forms.EmailInput(attrs={'placeholder': ' Эл. почта'}),
                   }
