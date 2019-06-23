"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import  serve
import xadmin

from django.urls import path, re_path, include
from django.views.generic import TemplateView
from MxShop.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls

from goods.views import GoodsListView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^xadmin', xadmin.site.urls)
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
    # 商品列表页
    url(r'goods/$', GoodsListView.as_view(), name="goods-list"),
    path('docs/', include_docs_urls(title="生鲜文档"))
]
