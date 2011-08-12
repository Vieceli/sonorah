
from settings import LOCAL,MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.defaults import patterns, include
#from feeds import UltimasNoticias

admin.autodiscover()

urlpatterns = patterns('',
 

    (r'^(robots.txt)$', 'django.views.static.serve', {'document_root': '/var/www/massivecoupon/'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
#(r'^rss/$', 'django.contrib.syndication.views.feed',  {'feed_dict': {'ultimos': UltimasNoticias} } ),
   #(r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
    #   {'feed_dict': {'ultimos': UltimasNoticias}}),
                    
     #includes
    (r'^$', include('principal.urls')),
    
   # (r'^/get_upload_progress^$', 'contato.views.get_upload_progress'),
    (r'^empresa/', include('empresa.urls')),
    (r'^portfolio/', include('portfolio.urls')),
    (r'^noticias/', include('noticias.urls')),
    (r'^artistas/', include('artistas.urls')),
    (r'^parceiros/', include('parceiros.urls')),
    (r'^conta/', include('contas.urls')),
    (r'^contato/', include('contato.urls')),
#    (r'^boleto/', include('boleto.urls')),#inseria midia propria -->url(r'imagem_barras/$', imagem_barras, name='imagem_barras'),
#    (r'^conta/', include('django.contrib.auth.urls')),
)

if LOCAL:
    urlpatterns = urlpatterns + patterns('',
        ((r'^media/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root': MEDIA_ROOT})),
                                  
        )
#    
handler404 = 'views.file_not_found_404'
handler500 = 'views.server_error_500'