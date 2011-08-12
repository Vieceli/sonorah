# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from contato.forms import ContatoForm


def contato(request,template_name):
    usuario=request.user
    url=str(request.get_full_path())
    pagina=url[1:-1]
    
#    if request.method == 'GET':
#        GET = request.GET  
#        if GET.has_key('a'):  
#            form = ArtistaForm(request.GET'  
#    
    if request.method == 'POST': 
        POST=request.POST
        print POST
        if POST.has_key('contato'):
            contato_form = ContatoForm(request.POST)
            if contato_form.is_valid(): 
                contato_form.save()
                return HttpResponseRedirect('/Obrigado/')
    else:
        contato_form = ContatoForm()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

