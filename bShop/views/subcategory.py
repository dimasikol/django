from django.shortcuts import render
from django.views import generic
from ..models import *

class SubCategoryView(generic.View):
    def get(self,request,*args,**kwargs):
        context = subcategory.SubCategory.objects.filter(category_id = kwargs['id'])
        return render(request,template_name='bShop/temp/list_sub_category.html', context={"object_list":context})
