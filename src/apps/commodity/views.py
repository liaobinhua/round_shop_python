from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommoditySerializer
from .models import Commodity
# Create your views here.


class GoodsListView(APIView):
    """
    List all goods
    """
    def get(self, request, format=None):
        goods = Commodity.objects.all()[:10]
        goods_serializers = CommoditySerializer(goods, many=True)
        return Response(goods_serializers.data)
