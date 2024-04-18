from django.contrib import admin
from .models import Profile , Skills , Team_Member
from django.utils.html import  format_html
# Register your models here.




@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name' , ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin) :

    list_display = ['full_name' , 'show_email' , 'phone'  ]


    def show_email(self , obj ):
        return obj.person.email

    show_email.short_description = "ایمیل"


@admin.register(Team_Member)
class Team_MemberAdmin(admin.ModelAdmin):
    list_display = ['show_img' , 'show_email' , 'show_username' ]



    def show_img(self , obj ) :
        return format_html('<img width=50px height=50px  src="{}">'.format(obj.team_member.picture.url))
    show_img.short_description = "تصویر کاربری"




    def show_email(self , obj ):
        return obj.team_member.person.email

    show_email.short_description = "ایمیل"


    def show_username(self , obj ):
        return obj.team_member.person.username

    show_username.short_description = "نام کاربری"