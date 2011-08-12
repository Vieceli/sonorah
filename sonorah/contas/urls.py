'''
Created on 13/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',    
    (r'^registrar/$', 'contas.views.registrar',  
        {'template_name': 'registration/registrar.html'},'registrar'),
    (r'^sair/$', 'contas.views.sair',  
        {},'sair'),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^entrar/$', 'login',
        {'template_name': 'registration/entrar.html'}, 'entrar'),
    
#    (r'^sair/$', 'logout',
#        {'template_name': 'registration/sair.html'}, 'sair'),
)