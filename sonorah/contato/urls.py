'''
Created on 14/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('contato.views',
          
        url(r'^$', 'contato', 
            {'template_name':'principal/contato.html'}, name='contato'),
                  
)