from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserAuthForm(AuthenticationForm):
    username = forms.CharField(label='')
    password = forms.CharField(widget=forms.PasswordInput, label='')
    class Meta:
        model = User
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'w3-input w3-round-large'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'w3-input w3-round-large'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='')
    password1 = forms.CharField(widget=forms.PasswordInput, label='')
    password2 = forms.CharField(widget=forms.PasswordInput, label='')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'w3-input w3-round-large'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'w3-input w3-round-large'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'w3-input w3-round-large'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'