# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from galeria.models import Foto,Album

def albuns(request):
    lista = Album.objects.all()
    
    return render_to_response('raiz/galeria/albuns.html', locals(), context_instance = RequestContext(request))

def album(request, slug):
    album = get_object_or_404(Album, slug = slug)
    imagens = Foto.objects.filter(album = album)
    
    return render_to_response('raiz/galeria/album.html', locals(), context_instance = RequestContext(request))

def imagem(request, slug):
    getFoto = get_object_or_404(Foto, slug = slug)
    
    return render_to_response('raiz/galeria/foto.html', locals(), context_instance = RequestContext(request))