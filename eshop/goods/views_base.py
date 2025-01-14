# -*- coding:utf-8 -*-
__author__ = 'xojisi'
__date__ = '2018/2/1 22:53'

from django.views.generic.base import View

from .models import Goods

class GoodsListView(View):
    def get(self,request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_list.append(json_dict)

        import json
        from django.core import serializers
        json_data = serializers.serialize("json",goods)
        json_data = json.loads(json_data)
        from django.http import JsonResponse

        return JsonResponse(json_data, safe=False)