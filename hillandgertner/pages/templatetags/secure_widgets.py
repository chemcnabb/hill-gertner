from django import template

register = template.Library()

@register.inclusion_tag('tags/carousel.html')
def image_gallery(protected_page):
    return {'protected_page': protected_page}
