from sonorah.artistas.models import Artista 
from django import template


register = template.Library()


#@register.inclusion_tag('lista_artista.html')
def lista_artista():
    artistas = Artista.objects.all();
    return {'artistas':artistas}

register.inclusion_tag('lista_artista.html')(lista_artista)