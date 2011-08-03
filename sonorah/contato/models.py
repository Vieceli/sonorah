# -*- coding: utf-8 -*- 
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from campo_personalizado import TelefoneField,ContentTypeRestrictedFileField


#OFERTA_IMG = 'cupon_imagens/'
#OFERTA_MINI = 'cupon_mini/'

class Contato(models.Model):
    class Meta:
        db_table = 'contato'
        verbose_name = _('Contato')
        verbose_name_plural = _('Contatos')
        
    nome            = models.CharField("Nome",max_length=40,
                              help_text=u'Nome',default='Lorem Ipsum')
    email           = models.EmailField()
    telefone        = models.CharField(u"Telefone",max_length=400,
                            help_text=u'Telefone',default='123456789', blank=True)
    arquivo         = models.FileField(upload_to='contato_arquivo', max_length=20,blank=True)
    mensagem        = models.TextField()
    criado_em       = models.DateTimeField(auto_now_add=True)
    atualizado_em   = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nome
    
