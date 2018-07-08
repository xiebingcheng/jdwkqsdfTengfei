from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import DetailView
import datetime

from .models import OneselfData, AlliancePartner, FamousPartner, FreeOpen, IntegrityNetworkTop,indexTopdata,WeChatQRCodeImg


# Create your views here.


class IndexView(View):
    # 首页获取数据并且渲染
    def get(self, request):
        all_oneselfdata = OneselfData.objects.all()
        all_alliancepartner = AlliancePartner.objects.all()
        all_famouspartner = FamousPartner.objects.all()
        all_freeopen = FreeOpen.objects.all()
        all_integritynetworktop = IntegrityNetworkTop.objects.all()
        all_indextopdata = indexTopdata.objects.all()
        # 获取服务器的时间
        time = datetime.datetime.now()

        return render(request, 'index.html', {
            'all_OneselfData': all_oneselfdata,
            'all_AlliancePartner': all_alliancepartner,
            'all_FamousPartner': all_famouspartner,
            'all_FreeOpen': all_freeopen,
            'all_IntegrityNetworkTop': all_integritynetworktop,
            'all_IndexTopData': all_indextopdata,
            'time': time,
        })


class LiuhecaiDetailView(View):
    # 详情页点击

    def get(self, request, detail_id):
        # 跳转到详情页 判断从哪个id跳转的详情页并取出数据放入详情页
        post_detail = OneselfData.objects.get(id=str(detail_id))
        # 获取服务器的时间
        time = datetime.datetime.now()
        # 为了获取微信二维码
        wechat_q_r_code_img = WeChatQRCodeImg.objects.all()

        # 实现上一篇和下一篇的功能
        has_prev = False
        has_next = False
        id_prev = id_next = int(detail_id)
        liuhecai_id_max = OneselfData.objects.all().order_by('-id').first()
        id_max = liuhecai_id_max.id
        # 有上一页的判断逻辑
        while not has_prev and id_prev >= 1:
            liuhecai_prev = OneselfData.objects.filter(id=id_prev - 1).first()
            if not liuhecai_prev:
                id_prev -= 1
            else:
                has_prev = True
        # 有下一页的判断逻辑
        while not has_next and id_next <= id_max:
            liuhecai_next = OneselfData.objects.filter(id=id_next +1).first()
            if not liuhecai_next:
                id_next += 1
            else:
                has_next = True

        return render(request, 'liuhecaiDetai.html', {
            # 传入详情页的数据
            'post_detail': post_detail,
            # 传入上下页的数据
            'liuhecai_prev': liuhecai_prev,
            'liuhecai_next': liuhecai_next,
            'has_prev': has_prev,
            'has_next': has_next,
            'time': time,
            # 获取微信二维码图片
            'WeChat_QR_code': wechat_q_r_code_img,
        })


# 想利用django的机制直接利用这个ArticleDetailView 类跳转到详情页 不过现在实现了
class ArticleDetailView(DetailView):
    pass

