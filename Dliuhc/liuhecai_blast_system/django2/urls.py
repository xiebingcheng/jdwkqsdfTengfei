"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin



from liuheziliao.views import IndexView,LiuhecaiDetailView
# 生产环境配置静态资源不经过django处理,直接nginx处理
# 线上部署
from django2.settings import STATIC_ROOT,MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^ht/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^detail/(?P<detail_id>\d+)/$',LiuhecaiDetailView.as_view(), name='detail'),
    # 微信二维码 等 图片地址
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 添加静态文件的访问处理函数
    url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT}),

]
