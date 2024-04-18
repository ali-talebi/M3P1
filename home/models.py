from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.




class Slider(models.Model):
    name = models.CharField(verbose_name="عنوان اسلایدر" , max_length = 100 )
    picture = models.FileField(verbose_name="تصویر" , upload_to = f"Silder/")


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'slider'
        verbose_name_plural = "تصاویر اسلایدر"



class Contact_Us(models.Model):

    status_choices = (
        ('no_response' , 'بدون پاسخ' ) ,
        ('in_response' , 'در حال پاسخ' ) ,
        ('out_response' , 'پاسخ داده شده')
    )
    name   = models.CharField(verbose_name="نام " , max_length = 100 )
    email  = models.EmailField(verbose_name="ایمیل" ,)
    text   = models.TextField(verbose_name="متن پیام" )
    status = models.CharField(verbose_name='وضعیت' , max_length =20 , choices=status_choices , default='no_response' )
    created = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



    class Meta :
        db_table = 'Contact_Us'
        verbose_name_plural = "تیکت ارتباط با ما"
