from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# class SignupForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()
#         fields = ('username', 'email', 'first_name', 'last_name')


# class MyUserChangeForm(UserChangeForm):
#     class Meta:
#         model = MyUser
#         fields = ('email', 'date_of_birth', 'password', 'is_active', 'is_admin')


# class UploadProfilePhotoForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['profile_photo']
#


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=63, label='username')
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='password')



