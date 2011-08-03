'''
Created on 14/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('parceiros.views',
          
        url(r'^$', 'parceiros', 
            {'template_name':'principal/parceiro.html'}, name='parceiros'),
            
        )