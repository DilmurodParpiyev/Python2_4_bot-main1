from django.contrib import admin
from myfiles.models import *
# Register your models here.
class AdminSubscribe(admin.ModelAdmin):
    list_display = ['id','ism','fam','username','tg_id']
admin.site.register(Subscribe,AdminSubscribe)

class AdminMenu(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Menu,AdminMenu)

class AdminMaxsulotlar(admin.ModelAdmin):
    list_display = ['id','nomi','rasm','malumot','tur']
admin.site.register(Maxsulotlar,AdminMaxsulotlar)

class AdminKorzinka(admin.ModelAdmin):
    list_display = ['id','nomi','rasm','malumot','tur','soni','username']
admin.site.register(Korzinka,AdminKorzinka)