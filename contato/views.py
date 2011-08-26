# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseBadRequest
from contato.forms import ContatoForm


def contato(request,template_name):
    usuario=request.user
    url=str(request.get_full_path())
    pagina=url[1:-1]
    
#    if request.method == 'GET':
#        GET = request.GET  
#        if GET.has_key('a'):  
#            form = ArtistaForm(request.GET'  
    if request.method == 'POST': 
        POST=request.POST
        contato_form = ContatoForm(request.POST,request.FILES)
        if contato_form.is_valid(): 
            #handle_uploaded_file(request.FILES['file'])
            print contato_form
            contato_form.save()
            return HttpResponseRedirect('/Obrigado/')
    else:
        contato_form = ContatoForm()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))



from django.core.cache import cache

def upload_progress(request):
    """
    Return JSON object with information about the progress of an upload.
    """
    progress_id = None
    if 'X-Progress-ID' in request.GET:
        progress_id = request.GET['X-Progress-ID']
    elif 'X-Progress-ID' in request.META:
        progress_id = request.META['X-Progress-ID']
    if progress_id:
        from django.utils import simplejson
        cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], progress_id)
        data = cache.get(cache_key)
        json = simplejson.dumps(data)
        return HttpResponse(json)
    else:
        return HttpResponseBadRequest('Server Error: You must provide X-Progress-ID header or query param.')
    
def get_upload_progress(request):
    from django.utils import simplejson
    cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], request.GET['X-Progress-ID'])
    data = cache.get(cache_key)
    return HttpResponse(simplejson.dumps(data))