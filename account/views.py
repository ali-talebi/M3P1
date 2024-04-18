from django.shortcuts import render ,redirect
from django.views import View
from .forms import LoginForm , RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.mixins import  LoginRequiredMixin

# Create your views here.




class LoginView(View) :




    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')

        return super().dispatch(request , *args , **kwargs )



    template_name = 'account/login/login.html'


    def get(self , request ):
        self.form = LoginForm
        content = {'form':self.form()}
        return render(request , self.template_name , content  )


    def post(self , request ):
        self.form = LoginForm
        self.form = self.form(request.POST)
        if self.form.is_valid() :
            user = authenticate(request , email = self.form.cleaned_data['email'] , password = self.form.cleaned_data['password'] )
            if user :
                login(request , user )
                messages.success(request , 'با موفقیت وارد شدید' , 'success')
                return redirect('home:home')
            else :
                messages.error(request , 'اطلاعات درست نیست ، شاید ثبت نام نکرده اید' , 'error')


        else :
            return redirect('home:home')
            messages.error(request , 'فرم درست پر نشده است' , 'error')



        content = {'from':self.form}
        return render(request , self.template_name , content  )




class RegisterView(View) :




    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')

        return super().dispatch(request , *args , **kwargs )




    template_name = 'account/register/register.html'
    form = RegisterForm

    def get(self ,request ) :

        content = {'form':self.form()}
        return render(request , self.template_name , content )


    def post(self , request ):
        self.form = self.form(request.POST)

        if self.form.is_valid() :
            User.objects.create_user(username=self.form.cleaned_data['username'] , email=self.form.cleaned_data['email'] , password=self.form.cleaned_data['password'])
            messages.success(request , 'ثبت نام شما با موفقیت انجام شد')
            return redirect('home:home' )

        else :
            messages.error(request , 'مشکلی در ثبت نام وجود دارد' , 'success' )



        content = {'form':self.form()}
        return render(request , self.template_name , content )



class LogoutView(LoginRequiredMixin , View) :



    def get(self , request ) :
        logout(request )
        messages.success(request , 'با موفقیت خارج شدید' , 'success')

        return redirect('home:home')




