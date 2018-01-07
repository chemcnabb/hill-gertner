
from django import template

register = template.Library()


@register.filter(name='cleanup_pages')
def cleanup_pages(obj):
    if obj:
        return obj
