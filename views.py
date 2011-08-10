from django.shortcuts import render_to_response
from django.template import RequestContext
def file_not_found_404(request):
    page_title = 'Pagina nao Encontrada'
    return render_to_response('404.html', locals(),
                              context_instance=RequestContext(request))
def server_error_500(request):
    page_title = u'Erro no Servidor'
    return render_to_response('500.html', locals(),
                              context_instance=RequestContext(request))   
    