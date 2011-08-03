# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Parceiro(models.Model):
    class Meta:
        db_table = 'parceiros'
        verbose_name = _('Parceiro')
        verbose_name_plural = _('Parceiros')
        
    nome            = models.CharField("Nome do Parceiro",max_length=40,
                              help_text=u'nome do Parceiro',default='Lorem Ipsum')
    empresa         = models.CharField("Nome da Empresa",max_length=40,
                              help_text=u'Nome da Empresa',default='Lorem Ipsum',blank=True,)
    site            = models.URLField(u"Seu site na web",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com',blank=True,)
    email           = models.EmailField()
    endereco        = models.CharField(u"Endereço",max_length=40,
                              help_text=u'Endereço',default='Lorem Ipsum')
    cidade          = models.CharField(u"Cidade",max_length=40,
                              help_text=u'Cidade',default='Lorem Ipsum')
    estado          = models.CharField(u"Estado",max_length=40,
                              help_text=u'Estado',default='Lorem Ipsum')
    telefone        = models.CharField(u"Telefone",max_length=400,
                            help_text=u'Telefone',default='123456789')
    mensagem        = models.TextField()
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome

class Radialista(models.Model):
    class Meta:
        db_table = 'radialistas'
        verbose_name = _('Radialista')
        verbose_name_plural = _('Radialistas')
        
    nome_radio      = models.CharField("Nome da Radio",max_length=40,
                              help_text=u'nome da Radio',default='Lorem Ipsum')
    frequencia      = models.CharField(u"Frequência da Radio",max_length=40,
                              help_text=u'Frequência da Radio',default='Lorem Ipsum')
    slogan          = models.CharField(u"Slogan da Radio",max_length=40,
                              help_text=u'Slogan da Radio',default='Lorem Ipsum')
    programador     = models.CharField(u"Programador da Radio",max_length=40,
                              help_text=u'Programador da Radio',default='Lorem Ipsum')
    direcao         = models.CharField(u"Direção da Radio",max_length=40,
                              help_text=u'Direção da Radio',default='Lorem Ipsum')
    email           = models.EmailField()
    telefone        = models.CharField(u"Telefone",max_length=400,
                            help_text=u'Telefone',default='123456789')
    endereco        = models.CharField(u"Endereço",max_length=40,
                              help_text=u'Endereço',default='Lorem Ipsum', blank=True)
    cidade          = models.CharField(u"Cidade",max_length=40,
                              help_text=u'Cidade',default='Lorem Ipsum')
    estado          = models.CharField(u"Estado",max_length=40,
                              help_text=u'Estado',default='Lorem Ipsum')
    mensagem        = models.TextField()
    anexo           = models.FileField(upload_to='radialista_arquivo', max_length=20971520, blank=True)
    site            = models.URLField(u"Site da radio",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com',blank=True,)
    facebook        = models.CharField(u"Facebook",max_length=400,
                              help_text=u'Facebook',default='Lorem Ipsum', blank=True)
    twitter         = models.CharField(u"Twitter",max_length=400,
                              help_text=u'Twitter',default='Lorem Ipsum', blank=True)
    youtube         = models.CharField(u"YouTube",max_length=400,
                              help_text=u'YouTube',default='Lorem Ipsum', blank=True)

    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome_radio
    
class Compositor(models.Model):
    class Meta:
        db_table = 'compositores'
        verbose_name = _('Compositor')
        verbose_name_plural = _('Compositores')
        
    nome            = models.CharField("Nome do Compositor",max_length=40,
                              help_text=u'nome do Compositor',default='Lorem Ipsum')
    arquivo         = models.FileField(upload_to='compositor_arquivo', max_length=20, blank=True)
    email           = models.EmailField()
    telefone        = models.CharField(u"Telefone",max_length=400,
                            help_text=u'Telefone',default='123456789')
    mensagem        = models.TextField()
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome
    
class Contratante(models.Model):
    class Meta:
        db_table = 'contratantes'
        verbose_name = _('Contratante')
        verbose_name_plural = _('Contratantes')
        
    nome            = models.CharField("Nome do Contratante",max_length=40,
                              help_text=u'Nome do Contratante',default='Lorem Ipsum')
    empresa         = models.CharField("Empresa do Contratante",max_length=40,
                              help_text=u'Empresa do Contratante',default='Lorem Ipsum',blank=True,)
    site            = models.URLField(u"Seu site na web",max_length=255,
                              help_text=u'http://site.com',default='http://www.globo.com',blank=True,)
    email           = models.EmailField()
    endereco        = models.CharField(u"Endereço",max_length=40,
                              help_text=u'Endereço',default='Lorem Ipsum')
    cidade          = models.CharField(u"Cidade",max_length=40,
                              help_text=u'Cidade',default='Lorem Ipsum')
    estado          = models.CharField(u"Estado",max_length=40,
                              help_text=u'Estado',default='Lorem Ipsum')
    telefone        = models.CharField(u"Telefone",max_length=400,
                            help_text=u'Telefone',default='123456789')
    mensagem        = models.TextField()
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome