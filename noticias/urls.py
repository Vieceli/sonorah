'''
Created on 14/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('noticias.views',
          
        url(r'^$', 'noticias', 
            {'template_name':'noticias/noticias.html'}, name='noticias'),
                  
        url(r'^(?P<noticia_slug>[-\w]+)/$', 'noticia', 
            {'template_name':'noticias/noticia.html'}, name='noticia'),
        )