'''
Created on 28/04/2011

@author: jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('principal.views',
                        #INDEX
  
                              
    url(r'^$', 'index', name='index'),     
    
#    url(r'^contato/$', 'contato', 
#        {'template_name':'principal/contato.html'}, name='contato'),   
)
