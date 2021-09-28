from django import forms


class RegForm(forms.Form):
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ИМЯ'}))
    surname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ФАМИЛИЯ'}))
    login = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ЛОГИН'}))
    password = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ПАРОЛЬ'}))
    repeat_password = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ПОВТОРИТЕ ПАРОЛЬ'}))


class AuthForm(forms.Form):
    login = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ЛОГИН'}))
    password = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ПАРОЛЬ'}))
