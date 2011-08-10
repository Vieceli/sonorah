# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext

def empresa(request,template_name):
    usuario=request.user
    url=str(request.get_full_path())
    nome_pagina=url[1:-1]
    pagina=nome_pagina
       
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))