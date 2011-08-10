# -*- coding: utf-8 -*- 
from django.db import models
from django.utils.translation import ugettext_lazy as _

#OFERTA_IMG = 'cupon_imagens/'
#OFERTA_MINI = 'cupon_mini/'

class Link(models.Model):
    class Meta:
        db_table = 'links'
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        
    titulo = models.CharField("Titulo do link",max_length=20,
                              help_text=u'Titulo do Link',default='Lorem Ipsum')
    url = models.URLField(u"Endereço na web",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com')
    slug = models.SlugField(unique=True)
    miniatura = models.ImageField(upload_to='mini_link/', blank=False)
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    ativo               = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.titulo

class Cadastra_Email(models.Model):
    class Meta:
        db_table = 'emails'
        verbose_name = _('Email Cadastrado')
        verbose_name_plural = _('Emails Cadastrados')
     
    def __unicode__(self):
        return self.email
    
    email           = models.EmailField(blank=True, help_text="Digite seu e-mail",default='Digite seu e-mail',unique=True)
    remover         = models.BooleanField(blank=True, default=False)