# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404

from django.template.context import RequestContext
from portfolio.models import Portfolio, Trabalhos
from artistas.models import Artista

def portfolios(request,template_name):
    usuario=request.user
    url=str(request.get_full_path())
    pagina=url[1:-1]
    portfolios = Portfolio.objects.all().order_by('-atualizado_em')
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def portfolio(request,template_name,portfolio_slug):
    usuario=request.user
    url=str(request.get_full_path())
    nome_pagina=url[1:-1]
    pagina=nome_pagina.rpartition('/')[0]
    noticia = nome_pagina.rpartition('/')[2]
    
    portfolio = get_object_or_404(Portfolio, slug=portfolio_slug)
    trabalhos = portfolio.trabalho.all().order_by('-atualizado_em')
    galerias=""
    for i in trabalhos:
        galerias = i.galeria.all()
    
    
    
    #trabalhos = Portfolio.objects.
    #ps=Portfolio.objects.filter(artista__slug__exact=artista_slug)#pega os portfolio somente do artista
    #p=Portfolio.objects.filter(artista__nome__exact='Lorem Ipsum')
#    for i in ps:
#    if i.genero=='V':
#        print "V"
#        print i
    portfolios_recentes = Portfolio.objects.all().order_by('-atualizado_em')
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))