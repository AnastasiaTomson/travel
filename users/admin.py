from django.contrib import admin
from .models import *

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from users.models import MyUser
from django.contrib.auth import authenticate


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': ' Пароль'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'placeholder': ' Повторите пароль'}))

    class Meta:
        model = MyUser
        fields = ('email', 'name', 'last_name', 'fathername', 'image')

        widgets = {'image': forms.FileInput(attrs={'onchange': 'ChangeImage(this)'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Имя'}),
                   'last_name': forms.TextInput(attrs={'placeholder': ' Фамилия'}),
                   'fathername': forms.TextInput(attrs={'placeholder': ' Отчество'}),
                   'email': forms.EmailInput(attrs={'placeholder': ' Эл. почта (Логин)'}),
                   }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    class Meta:
        model = MyUser
        fields = ('email', 'name', 'last_name', 'fathername', 'image')

        widgets = {'image': forms.FileInput(attrs={'onchange': 'ChangeImage(this)'}),
                   'name': forms.TextInput(attrs={'placeholder': ' Имя'}),
                   'last_name': forms.TextInput(attrs={'placeholder': ' Фамилия'}),
                   'fathername': forms.TextInput(attrs={'placeholder': ' Отчество'}),
                   'email': forms.EmailInput(attrs={'placeholder': ' Эл. почта (Логин)'}),
                   }

    def clean_password2(self, user):
        # Check that the two password entries match
        password_old_value = self.cleaned_data.get("password_old")
        password1_new_value = self.cleaned_data.get("password1_new")
        password2_new = self.cleaned_data.get("password2_new")
        if not user.check_password(password_old_value):
            self.add_error('password_old', "Старый пароль не совпадает")
        elif password1_new_value and password2_new and password1_new_value != password2_new:
            self.add_error('password1_new', "Новые пароли не совпадают")
        else:
            return password2_new

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserEditForm, self).save(commit=False)
        # user.set_password(self.cleaned_data["password1_new"])
        if commit:
            user.save()
        return user


class UserEditPasswordForm(forms.Form):
    password_old = forms.CharField(label='Введите старый пароль',
                                   widget=forms.PasswordInput(attrs={'placeholder': ' Пароль'}))
    password1_new = forms.CharField(label='Введите новый пароль',
                                    widget=forms.PasswordInput(attrs={'placeholder': ' Пароль'}))
    password2_new = forms.CharField(label='Повторите новый пароль',
                                    widget=forms.PasswordInput(attrs={'placeholder': ' Повторите пароль'}))

    def clean_password2(self, user):
        password_old_value = self.cleaned_data.get("password_old")
        password1_new_value = self.cleaned_data.get("password1_new")
        password2_new = self.cleaned_data.get("password2_new")
        if not user.check_password(password_old_value):
            self.add_error('password_old', "Старый пароль не совпадает")
        elif password1_new_value and password2_new and password1_new_value != password2_new:
            self.add_error('password1_new', "Новые пароли не совпадают")
        else:
            return password2_new

    def save(self, user):
        user.set_password(self.cleaned_data["password1_new"])
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'name', 'last_name', 'fathername', 'image', 'is_active', 'is_admin')
        widgets = {'image': forms.FileInput}

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin', 'name', 'last_name', 'fathername', 'image')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('name', 'last_name', 'fathername', 'image')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'image', 'name', 'last_name', 'fathername')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email', 'name', 'last_name', 'fathername', 'image')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
