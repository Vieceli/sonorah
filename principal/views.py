# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from noticias.models import Noticia
from principal.models import Link, Musica


def index(request):
    usuario=request.user
    url=request.get_full_path
    noticias = Noticia.objects.all().order_by('-atualizado_em')[:5]
    links = Link.objects.all().order_by('-atualizado_em')[:5]

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def radio(request, template_name):
    usuario=request.user
    url=request.get_full_path
    musicas = Musica.objects.all().order_by('-atualizado_em')[:5]
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def obrigado(request, template_name):
    usuario=request.user
    url=request.get_full_path
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


