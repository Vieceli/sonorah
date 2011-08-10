'''
Created on 19/07/2011

@author: jhoni
'''
from django.contrib.syndication.feeds import Feed
from noticias.models import Noticia
from django.utils import feedgenerator


#class UltimasNoticias(Feed):
#    title = 'Ultimas noticias do Sonorah'
#    link = '/'
#    description = 'Sistema de noticia do Sonorah'
#    description_template = 'feeds/beat_description.html'
#    feed_type = feedgenerator.Rss201rev2Feed
#    
#    def items(self):
#        return Noticia.objects.order_by('-criado_em')[:5]
#
#    def item_link(self, object):
#        return '/noticias/%d/'%object.id
#    
#    def item_title(self, object):
#        return object.title
##
#    def item_description(self, object):
#        return object.description