# Create your views here.
from parceiros.forms import ContratantesForm, CompositoresForm, RadialistaForm,\
    ParceiroForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.forms.formsets import formset_factory

def parceiros(request,template_name):
    usuario=request.user
    url=str(request.get_full_path())
    pagina=url[1:-1]
    valido=True
    
    if request.method == 'POST': 
        POST=request.POST
        contratante_form = ContratantesForm(request.POST,request.FILES)
        compositor_form = CompositoresForm(request.POST,request.FILES)
        radialista_form = RadialistaForm(request.POST,request.FILES)
        parceiro_form = ParceiroForm(request.POST,request.FILES)
        
        if POST.has_key('contratante'):
            #print "POST['contratante']"       
            if contratante_form.is_valid(): 
                contratante_form.save()
                return HttpResponseRedirect('/Obrigado/')
            else:
                valido=False
                opcao="contratante"
                contratante_form = ContratantesForm(request.POST)
        elif POST.has_key('compositor'):
            #print "POST['compositor']"
            if compositor_form.is_valid(): 
                compositor_form.save()
                return HttpResponseRedirect('/Obrigado/')
            else:
                valido=False
                opcao="compositor"
                compositor_form = CompositoresForm(request.POST)
        elif POST.has_key('radialista'):
            #print "POST['radialista']"
            if radialista_form.is_valid(): 
                radialista_form.save()
                return HttpResponseRedirect('/Obrigado/')
            else:
                valido=False
                opcao="radialista"
                radialista_form = RadialistaForm(request.POST)
        elif POST.has_key('parceiro'):
            #print "POST['parceiro']"
            if parceiro_form.is_valid(): 
                parceiro_form.save()
                return HttpResponseRedirect('/Obrigado/')
            else:
                valido=False
                opcao="parceiro"
                parceiro_form = ParceiroForm(request.POST)
       
    else:
        contratante_form = ContratantesForm() 
        compositor_form = CompositoresForm()
        radialista_form = RadialistaForm()
        parceiro_form = ParceiroForm() 

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

#        contratante_form_set = ContratantesForm(POST, request.FILES, prefix="contratante")
#        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
#        print POST
#        if POST['compositor']:
#            print "olaa compositor"
#    if request.method == 'GET':
#        GET = request.GET  
#        if GET.has_key('a'):  
#            form = ArtistaForm(request.GET'  
# 
#    contratante_form_set = formset_factory(ContratantesForm)
#    compositor_form_set  = formset_factory(CompositoresForm)
#    radialista_form_set  = formset_factory(RadialistaForm)
#    parceiro_form_set    = formset_factory(ParceiroForm)