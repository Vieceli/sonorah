# Create your views here.
from artistas.forms import ArtistaForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from artistas.models import Artista

def artistas(request,template_name):
    artistas = Artista.objects.all().order_by('-atualizado_em')
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def vcnosonorah(request,template_name):
    usuario=request.user
    if request.method == 'POST': 
        POST=request.POST
        print POST
        artista_form = ArtistaForm(request.POST)
        if artista_form.is_valid(): 
            artista_form.save()
            return HttpResponseRedirect('/Obrigado/')
       
    else:
        artista_form = ArtistaForm()
        
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

