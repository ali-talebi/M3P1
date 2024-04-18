from django.contrib import admin
from .models import Slider , Contact_Us
from django.utils.html import format_html
# Register your models here.


@admin.register(Contact_Us)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'created_show'  )

    def created_show(self , obj ):
        return obj.created.strftime('%B %d, %Y - %I:%M:%S %p')



@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name' , 'show_img')

    def show_img(self, obj):
        return format_html('<img width=50px heigth=50px src="{}">'.format(obj.picture.url))