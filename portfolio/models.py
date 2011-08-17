# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from photologue.models import Gallery, GalleryUpload

 
class Portfolio(models.Model):
    class Meta:
        db_table = 'portfolio'
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolio')
    
    titulo              = models.CharField("Titulo do Portfolio",max_length=255,
                              help_text=u'Titulo do Portfolio',default='Hitallo e Elan')    
    imagem              = models.ImageField(upload_to='imagem_portfolio/', blank=False, help_text=u'Imagem representativa')
    descricao           = models.CharField("Descricao do Portfolio",max_length=255,
                              help_text=u'Descricao do Portfolio',default='Lorem ipsum dolor sit amet! Lorem ipsum dolor sit amet!')
    slug                = models.SlugField(unique=True)
   
    ordem               = models.IntegerField(default=0)
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    teste = models.ForeignKey('self')
    
    def __unicode__(self):
        return self.titulo
    
    # def get_absolute_url(self):
    #     return reverse('noticias', kwargs={'noticia_slug': self.pk})
    def get_absolute_url(self):
        return reverse('portfolio', kwargs={'portfolio_slug': self.slug})
#    def get_absolute_url(self):
#        return (u'noticias', (), { u'noticia_slug': self.slug })

class Trabalhos(models.Model):
    class Meta:
        db_table = 'trabalho'
        verbose_name = _('Trabalho')
        verbose_name_plural = _('Trabalhos')
    
    
       
    titulo              = models.CharField("Nome para o trabalho",max_length=255,
                              help_text=u'Nome para o trabalho',default='Hitallo e Elan', blank=True)  
    link_video          = models.URLField(u"Link YouTube",max_length=255,
                              help_text=u'http://www.youtube.com/watch?v=65B6qyz6IQ4', blank=True)
    url                 = models.URLField(u"Endereço na web do portfolio",max_length=255,
                              help_text=u'http://sitedoportfolio.com', blank=True)
    galeria             = models.ManyToManyField(Gallery, blank=True)
    slug                = models.SlugField(unique=True)
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    portfolios          = models.ForeignKey(Portfolio)
    
    def __unicode__(self):
        return self.titulo
    
    # def get_absolute_url(self):
    #     return reverse('noticias', kwargs={'noticia_slug': self.pk})
    def get_absolute_url(self):
        return reverse('portfolio', kwargs={'portfolio_slug': self.slug})
    