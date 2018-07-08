from django.db import models

# Create your models here.


class TheMainInformation(models.Model):
    title = models.CharField('主站标题',max_length=150)
    main_url = models.URLField('跳转连接地址',max_length=150)

    class Meta:
        verbose_name = '99站点跳转链接管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


