# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
import os
from urllib import pathname2url, url2pathname
from django.template.context import RequestContext
from noticias.models import Noticia


def noticias(request,template_name):
    usuario=request.user
    url=str(request.get_full_path())
    pagina=url[1:-1]
    noticias = Noticia.objects.all().order_by('-atualizado_em')
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def noticia(request,template_name,noticia_slug):
    usuario=request.user
    url=str(request.get_full_path())
    nome_pagina=url[1:-1]
    pagina=nome_pagina.rpartition('/')[0]
    nome_interno = nome_pagina.rpartition('/')[2]
    noticia = get_object_or_404(Noticia, slug=noticia_slug)
    noticias_recentes = Noticia.objects.all().order_by('-atualizado_em')
    
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))