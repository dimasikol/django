from django import template
from ..models import *


register = template.Library()

@register.simple_tag
def category_tags():
    model = Category.objects.all()
    return model