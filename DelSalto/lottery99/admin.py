from django.contrib import admin

from .models import TheMainInformation
# Register your models here.


admin.site.register(TheMainInformation)

admin.site.site_header = '99娱乐站点首页跳转后台系统'
admin.site.site_title = '99娱乐站点首页跳转后台系统'