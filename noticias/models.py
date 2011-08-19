from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Noticia(models.Model):
    class Meta:
        db_table = 'noticias'
        verbose_name = _('Noticia')
        verbose_name_plural = _('Noticias')
        
    titulo              = models.CharField("Titulo",max_length=255,
                              help_text=u'Titulo da noticia',default='Lorem Ipsum')
    subtitulo           = models.CharField("Subtitulo",max_length=255,
                              help_text=u'Subtitulo da noticia',default='Lorem ipsum dolor sit amet!')
    texto               = models.TextField("Texto da Noticia")
    imagem              = models.ImageField(upload_to='noticia/', blank=False)
    miniatura           = models.ImageField(upload_to='mini_noticia/', blank=False)
    
    slug                = models.SlugField(unique=True)
    meta_description    = models.CharField("Descricao da noticia para o google",max_length=255,
                              help_text=u'Descricao da noticia para o google',default='Lorem ipsum dolor sit amet!')
    meta_keywords       = models.CharField("Palavras chave da noticia para o google",max_length=255,
                              help_text=u'Palavras chave da noticia para o google',default='Lorem ipsum dolor sit amet!')
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.titulo
    
    # def get_absolute_url(self):
    #     return reverse('noticias', kwargs={'noticia_slug': self.pk})
    def get_absolute_url(self):
        return reverse('noticias', kwargs={'noticia_slug': self.slug})
#    def get_absolute_url(self):
#        return (u'noticias', (), { u'noticia_slug': self.slug })