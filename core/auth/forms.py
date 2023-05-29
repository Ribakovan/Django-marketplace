from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

INPUT_CLASSES = 'my-3 w-full py-4 px-6 rounded-xl border'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин',
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': INPUT_CLASSES
    }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин',
        'class': INPUT_CLASSES
    }), label='Логин')
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Почта',
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль',
        'class': INPUT_CLASSES
    }))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'phone_num', 'city')

        widgets = {
            'avatar': forms.FileInput(attrs={
                'required': False,
                'placeholder': 'Аватар',
                'class': INPUT_CLASSES
            }),
            'phone_num': forms.TextInput(attrs={
                'required': False,
                'placeholder': 'Номер телефона',
                'class': INPUT_CLASSES
            }),
            'city': forms.Select(attrs={
                'required': False,
                'placeholder': 'Город',
                'class': INPUT_CLASSES
            }),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Почта',
        'class': INPUT_CLASSES
    }), required=False, label='Почта')
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя',
        'class': INPUT_CLASSES
    }), required=False, label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Фамилия',
        'class': INPUT_CLASSES
    }), required=False, label='Фамилия')
