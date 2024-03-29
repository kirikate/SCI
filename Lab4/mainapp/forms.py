from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(forms.Form):
    dateBegin = forms.DateField(widget=forms.SelectDateWidget())
    timeBegin = forms.TimeField(widget=forms.TimeInput)
    dateEnd = forms.DateField(widget=forms.SelectDateWidget)
    timeEnd = forms.TimeField()
    
    class Meta:
        fields = ('dateBegin', 'dateEnd')
        widgets = {
            'dateBegin': forms.DateTimeField(),
            'dateEnd': forms.DateTimeField()
        }

# class LoginForm(forms.Form):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(
#         attrs={'class': 'form-input'}))
#     password1 = forms.CharField(
#         label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-input'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-input'}),
#         }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    f = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    i = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    o = forms.CharField(label='Отчество', widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    adress = forms.CharField(
        label='Адрес', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = forms.CharField(
        label='Телефонный номер (+375(XX)XXXXXXX)', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'f', 'i', 'o', 'phone', 'adress', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'f':forms.TextInput(attrs={'class':'form-input'}),
            'i': forms.TextInput(attrs={'class': 'form-input'}),
            'o': forms.TextInput(attrs={'class': 'form-input'}),
            'phone':forms.TextInput(attrs={'class':'form-input'}),
            'adress':forms.TextInput(attrs={'class':'form-input'}),
            'password1':forms.PasswordInput(attrs={'class':'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }