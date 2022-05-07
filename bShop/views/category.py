from django.shortcuts import render
from django.views import generic
from ..models import *

class CategoryView(generic.ListView):
    model = category.Category
    template_name = 'bShop/temp/list_category.html'
    context_object_name = 'object_list'

