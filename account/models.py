from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.




class Profile(models.Model) :


    person    = models.OneToOneField(User , verbose_name="فرد مورد نظر" , on_delete=models.CASCADE )
    full_name = models.CharField(verbose_name="اسم کامل" , max_length= 100 , default='بذون نام' )
    phone     = models.CharField(verbose_name= "للفن همراه" , max_length = 11 , default='-' )
    picture   = models.FileField(verbose_name="تصویر" , upload_to=f"Profile/Picture/" , null=True , blank=True )


    def __str__(self ):
        return self.person.username

    class Meta :
        db_table = "Profile"
        verbose_name_plural = "پروفایل کاربری افراد"


class Skills(models.Model):
    name = models.CharField(verbose_name="نام مهارت" , max_length=15 )

    def __str__(self):
        return self.name
    class Meta :
        db_table = 'skills'
        verbose_name_plural = "مهارت های اعضا"


class Team_Member(models.Model):
    team_member = models.ForeignKey(Profile , on_delete=models.CASCADE , verbose_name="فرد")
    introduce   = models.CharField(verbose_name="معرفی نامه" , max_length=120 )
    skills = models.ManyToManyField(Skills , null=True )
    description = RichTextField(verbose_name="توضیحات درباره معرفی جامع عضو تیم" , null=True, blank=True)
    linkedin = models.CharField(verbose_name="لینکدین" , null=True, blank=True, max_length=50 )
    instagram = models.CharField(verbose_name="اینستاگرام" , null=True, blank=True, max_length=50 )




    def __str__(self):
        return self.team_member.full_name

    class Meta :
        db_table = 'Team_Member'
        verbose_name_plural = "اعضای تیم"




