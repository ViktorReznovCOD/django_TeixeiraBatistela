from django import template

from scmp.models import Noticia

register = template.Library()

@register.inclusion_tag('scmp/partials/index.html')
def noticias(takes_context=True):
    ultimas_noticias = Noticia.objects.order_by('data')[:3]
    return {'ultimas_noticias': ultimas_noticias}