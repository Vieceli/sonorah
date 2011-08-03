'''
Created on 14/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('artistas.views',
          
        url(r'^$', 'artistas', 
            {'template_name':'artistas/artistas.html'}, name='artistas'),
                  
        url(r'^vcnosonorah/$', 'vcnosonorah', 
            {'template_name':'artistas/vcnosonorah.html'}, name='vcnosonorah'),
        )