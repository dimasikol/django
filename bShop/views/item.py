from django.shortcuts import render
from django.views import generic
from ..models import *
class ItemListView(generic.View):
    def get(self,request,*args,**kwargs):
        context = item.Item.objects.filter(sub_category=kwargs['id'])
        return render(request,template_name='bShop/temp/list_item_category.html',context={'object_list':context})

class ItemView(generic.View):
    def get(self,request,*args,**kwargs):
        context = item.Item.objects.get(url=kwargs['url'])
        return render(request,template_name='bShop/temp/detail_item.html',context={'object':context})
