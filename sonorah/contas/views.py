# Create your views here.
from sonora_portal001.contas.forms import FormularioRegistro, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.views import login, logout
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.simple import direct_to_template

def registrar(request, template_name):
    page_title = 'Registro de Usuario'
    """  Registra o Usuario """
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = FormularioRegistro(postdata)
        if form.is_valid():
            
            cd = form.cleaned_data
            user = User()
            user.username = cd.get('usuario')
            user.email = cd.get('email2')
            user.set_password( cd.get('senha2') )
            user.save()
            try:
                user = authenticate(username=user.username, password=user.password)
            except Exception, e:
                print e

            #form.envia_email() ################### enviar email           
            #redireciona para minha conta efetuando login
            if user is not None:
                print "teste"
                print user
                if user.is_active:
                    login(request, user)
                    #redireciona para pagina de sucesso
                    url = urlresolvers.reverse('perfil')
                    return HttpResponseRedirect(url)
                else:
                    #redireciona para conta desabilitada
                    pass
                    #return direct_to_template(request, 'inactive_account.html')
            else:
                #redireciona para login invalido
                pass
                #return direct_to_template(request, 'invalid_login.html')
    else:
        form = FormularioRegistro()
    
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def entrar(request, template_name):
    state = "Efetue Login"
    if request.method == 'POST': # If the form has been submitted...
        postdata = request.POST.copy()
        form_login = LoginForm(postdata) 
        if form_login.is_valid():
            cd = form_login.cleaned_data
            email = cd.get('email')
            senha =  cd.get('senha')
            user = authenticate(username=email, password=senha)   
            if user is not None and user.is_active:
                    login(request, user)
    
                    if request.POST['next']:
                        return HttpResponseRedirect(request.POST['next'])
                    else:
                        return HttpResponseRedirect('/')
                    
                    return HttpResponseRedirect('/')
            else:    
                return direct_to_template(request, 'invalid_login.html')

            return HttpResponseRedirect('/')  

    else:
        initial_data = {}
        form_login = LoginForm(initial=initial_data)


    return render_to_response(template_name, {
                'form_login' : form_login,
                'state':state,
              }, context_instance=RequestContext( request ) )

def sair(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")