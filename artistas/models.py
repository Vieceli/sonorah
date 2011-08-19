# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Artista(models.Model):
    class Meta:
        db_table = 'artistas'
        verbose_name = _('Artista')
        verbose_name_plural = _('Artistas')
        
    nome                = models.CharField("Nome",max_length=255,
                              help_text=u'Nome do Artista',default='Lorem Ipsum')
    imagem              = models.ImageField(upload_to='img_artista/', blank=False)
    site                = models.URLField(u"Endereço do Site do Artista",max_length=255,
                              help_text=u'http://www.artista.com',default='http://www.artista.com')
    facebook            = models.URLField(u"Endereço do Facebook",max_length=255,
                              help_text=u'http://www.facebook.com',default='http://www.facebook.com', blank=True)
    twitter             = models.URLField(u"Endereço do Twiiter",max_length=255,
                              help_text=u'http://www.twitter.com',default='http://www.twitter.com', blank=True)
    myspace             = models.URLField(u"Endereço do MySpace",max_length=255,
                              help_text=u'http://www.myspace.com',default='http://www.myspace.com', blank=True)
    youtube             = models.URLField(u"Endereço do Youtube",max_length=255,
                              help_text=u'http://www.youtube.com',default='http://www.youtube.com', blank=True)
    slug                = models.SlugField(unique=True)
    meta_description    = models.CharField("Descricao do artista para o google",max_length=255,
                              help_text=u'Descricao do artista para o google',default='Lorem ipsum dolor sit amet!')
    meta_keywords       = models.CharField("Palavras chave da noticia para o google",max_length=255,
                              help_text=u'Palavras chave da noticia para o google',default='Lorem ipsum dolor sit amet!')
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome
    
    #def get_absolute_url(self):
    #     return reverse('noticias', kwargs={'noticia_slug': self.pk})
    def get_absolute_url(self):
        return reverse('artista', kwargs={'artista_slug': self.slug})
#    def get_absolute_url(self):

class Artista_Contato(models.Model):
    class Meta:
        db_table = 'artista_contato'
        verbose_name = _('Artista_em_contato')
        verbose_name_plural = _('Artistas_em_contato')
        
    nome            = models.CharField("Nome do Artista",max_length=40,
                              help_text=u'Nome do Artista',default='Lorem Ipsum')
    site            = models.URLField(u"Seu site na web",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com',blank=True)
    email           = models.EmailField()
    endereco        = models.CharField(u"Endereço",max_length=40,
                              help_text=u'Endereço',default='Lorem Ipsum')
    cidade          = models.CharField(u"Cidade",max_length=40,
                              help_text=u'Cidade',default='Lorem Ipsum')
    estado          = models.CharField(u"Estado",max_length=40,
                              help_text=u'Estado',default='Lorem Ipsum')
    telefone        = models.CharField(u"Telefone",max_length=400,
                              help_text=u'Telefone',default='123456789')
    arquivo         = models.FileField(upload_to='artista_arquivo', max_length=20)
    facebook        = models.CharField(u"Facebook",max_length=400,
                              help_text=u'Facebook',default='Lorem Ipsum', blank=True)
    twitter         = models.CharField(u"Twitter",max_length=400,
                              help_text=u'Twitter',default='Lorem Ipsum', blank=True)
    youtube         = models.CharField(u"YouTube",max_length=400,
                              help_text=u'YouTube',default='Lorem Ipsum', blank=True)
    mensagem        = models.TextField()
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome