'''
Created on 14/07/2011

@author: Jhoni
'''
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('contato.views',
          
        url(r'^$', 'contato', 
            {'template_name':'principal/contato.html'}, name='contato'),
                       
        url(r'^get_upload_progress?.*$', 'get_upload_progress'),         
        #url(r'^(?P<X-Progress-ID>[-\w]+)/$', 'get_upload_progress', name='get_upload_progress'),
         #    r'^/get_upload_progress^$', 'contato.views.get_upload_progress'),     
)