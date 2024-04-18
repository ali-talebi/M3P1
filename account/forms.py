



from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form) :


    username    = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder' : 'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'رمز عبور'}))



class RegisterForm(forms.Form) :

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'نام کاربری' }))
    email    = forms.EmailField(widget=forms.EmailInput(attrs = {'class':'form-control' , 'placeholder':'ایمیل'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'رمز عبور'}))




    def clearn_username(self):
        select_username = self.cleaned_data['username']
        user = User.objects.filter(username=select_username).exists()
        if user :
            raise ValidationError("نام کاربری قبلا انتخاب شده است")

        return select_username


    def clean_email(self):

        select_email = self.cleaned_data['email']
        user = User.objects.filter(email = select_email ).exists()
        if user :
            raise ValidationError('ایمیل قبلا ثبت نام کرده است')
        return select_email







