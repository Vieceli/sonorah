'''
Created on 14/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('empresa.views',
          
        url(r'^$', 'empresa', 
            {'template_name':'empresa.html'}, name='empresa'),
                  
       )