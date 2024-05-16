from django import template
from ..models import NameMod

register = template.Library()

@register.simple_tag()
def category_tag():
    return NameMod.objects.all()
