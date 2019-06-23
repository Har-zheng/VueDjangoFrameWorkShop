from .serializers import GoodsSerializers
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics

from .models import Goods

# Create your views here.
class GoodsListView(mixins.ListModelMixin,  generics.GenericAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)