from django.apps import AppConfig
import os


# 修改admin的列表名

default_app_config = 'liuheziliao.PrimaryBlogConfig'
VERBOSE_APP_NAME = u"六合彩爆料系统站点管理"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class PrimaryBlogConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME