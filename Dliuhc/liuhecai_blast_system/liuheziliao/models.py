from django.db import models

# Create your models here.


class OneselfData(models.Model):
    # 今晚免费精准资料 数据库定义
    name = models.CharField(max_length=120, verbose_name="资料标题")
    content = models.TextField(verbose_name='正文', default='')


    class Meta:
        verbose_name = "今晚免费精准资料"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AlliancePartner(models.Model):
    # 推荐同盟合作站
    name = models.CharField(max_length=120, verbose_name="合作站标题")
    url = models.URLField(max_length=300, verbose_name="合作站跳转地址")

    class Meta:
        verbose_name = '推荐同盟合作站'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FamousPartner(models.Model):
    # 名站大流量合作
    name = models.CharField(max_length=120, verbose_name="名站大流量合作区")
    url = models.URLField(max_length=300, verbose_name="名站大流量合作站跳转地址")

    class Meta:
        verbose_name = '名站大流量合作'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FreeOpen(models.Model):
    # 免费公开资料
    name = models.CharField(max_length=120, verbose_name="免费公开资料")
    url = models.URLField(max_length=300, verbose_name="免费公开资料跳转地址")

    class Meta:
        verbose_name = '免费公开资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IntegrityNetworkTop(models.Model):
    # 诚信网投专区
    name = models.CharField(max_length=120, verbose_name="诚信网投专区")
    url = models.URLField(max_length=300, verbose_name="网投专区链接跳转地址")

    class Meta:
        verbose_name = '诚信网投专区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class indexTopdata(models.Model):
    # 首页上部广告位
    name = models.CharField(max_length=120, verbose_name="首页上部广告位标题")
    url = models.URLField(max_length=300, verbose_name="首页上部广告位置跳转地址" )

    class Meta:
        verbose_name = "首页最上部广告位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class WeChatQRCodeImg(models.Model):
    # 微信二维码图片上传
    name = models.CharField(max_length=120, verbose_name="微信二维码说明")
    # 微信二维码图片
    wechat_img_qr_code = models.ImageField(upload_to='img',verbose_name="微信二维码图片上传地址")

    class Meta:
        verbose_name = '微信二维码图片上传'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

