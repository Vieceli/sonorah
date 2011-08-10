'''
Created on 28/04/2011

@author: jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('principal.views',
                        #INDEX         
    url(r'^$', 'index', name='index'),     
#    url(r'^links/$', 'links', 
#        {'template_name':'principal/links.html'}, name='links'),
#    url(r'^contato/$', 'contato', 
#        {'template_name':'principal/contato.html'}, name='contato'),   
)
