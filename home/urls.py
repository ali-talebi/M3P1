from django.urls import  path
from .views import *
app_name = "home"


urlpatterns = [
    path( '' , Home.as_view() , name="home" ) ,
    path('contact_us/' , Contact_usView.as_view(), name="contactus") ,
]