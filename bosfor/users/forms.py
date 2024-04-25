from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Адрес электронной почты', widget = forms.TextInput(attrs={
        'class': 'form-control py-1', 'placeholder': 'Введите адрес эл.почты'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class':'form-control py-1', 'placeholder': 'Введите пароль'}))    

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Адрес электронной почты', widget = forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите адрес эл.почты'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder': 'Введите пароль'}))   
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder': 'Повторно введите пароль'}))   

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget = forms.FileInput(attrs={'class': 'form-control py-4'}), required=False)
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True})) 

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')