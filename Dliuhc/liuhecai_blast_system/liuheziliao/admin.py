from django.contrib import admin

from .models import IntegrityNetworkTop,OneselfData,AlliancePartner,FamousPartner,FreeOpen,indexTopdata,WeChatQRCodeImg
# Register your models here.

# 原始的admin 下面需要该名字 所以需要这样改
admin.site.register(IntegrityNetworkTop)
admin.site.register(OneselfData)
admin.site.register(AlliancePartner)
admin.site.register(FamousPartner)
admin.site.register(FreeOpen)
admin.site.register(indexTopdata)
admin.site.register(WeChatQRCodeImg)

admin.site.site_header = '六合彩爆料管理系统'
admin.site.site_title = '六合彩料管理'


# 需要更改admin后台的名称
# class MyAdminSite(admin.AdminSite):
#     site_header = "我的管理网站"
#
#
# admin_site = MyAdminSite()
#
# admin_site.register(IntegrityNetworkTop)
# admin_site.register(OneselfData)
# admin_site.register(AlliancePartner)
# admin_site.register(FamousPartner)
# admin_site.register(FreeOpen)
# admin_site.register(indexTopdata)


