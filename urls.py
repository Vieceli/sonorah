
from settings import LOCAL,MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.defaults import patterns, include
from feeds import UltimasNoticias

feeds = {
    'ultimos': UltimasNoticias
}

admin.autodiscover()

urlpatterns = patterns('',
    
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^municipios_app/', include('municipios.urls')),
    (r'^photologue/', include('photologue.urls')),
    (r'^(robots.txt)$', 'django.views.static.serve', {'document_root': '/var/www/massivecoupon/'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
                          
    (r'^radio/$', 'principal.views.radio', {'template_name':'principal/radio.html'}, 'radio'),

                    
     #includes
    (r'^$', 'views.manutencao'),
    (r'^beta/$', include('principal.urls')),
    
   # (r'^/get_upload_progress^$', 'contato.views.get_upload_progress'),
    (r'^beta/empresa/', include('empresa.urls')),
    (r'^beta/portfolio/', include('portfolio.urls')),
    (r'^beta/noticias/', include('noticias.urls')),
    (r'^beta/artistas/', include('artistas.urls')),
    (r'^beta/parceiros/', include('parceiros.urls')),
    (r'^beta/conta/', include('contas.urls')),
    (r'^beta/contato/', include('contato.urls')),
#    (r'^boleto/', include('boleto.urls')),#inseria midia propria -->url(r'imagem_barras/$', imagem_barras, name='imagem_barras'),
#    (r'^conta/', include('django.contrib.auth.urls')),
)
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#urlpatterns += staticfiles_urlpatterns()
if LOCAL:
    urlpatterns = urlpatterns + patterns('',
        ((r'^media/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root': MEDIA_ROOT})),
                                  
        )
#    
handler404 = 'views.file_not_found_404'
handler500 = 'views.server_error_500'