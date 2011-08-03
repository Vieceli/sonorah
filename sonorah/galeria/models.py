from django.db import models
import os
import random
import shutil
import zipfile

# Create your models here.

from django.core.urlresolvers import reverse 
from django.db import models
from datetime import datetime
from utils.thumbs import ImageWithThumbsField
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile

    
class Album(models.Model):
    titulo = models.CharField(u'Titulo', max_length = 100)
    slug = models.SlugField(max_length = 100, blank = True, unique = True)
    data = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):   
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('album', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('titulo', )
        db_table = 'psssv_album' 
        verbose_name_plural = 'Albuns'

class Foto(models.Model):
    album = models.ForeignKey('Album')
    titulo = models.CharField(u'Titulo', max_length = 100)
    slug = models.SlugField(max_length = 100, blank = True, unique = True)
    descricao = models.TextField(blank = True)
    original = ImageWithThumbsField(
        null = True,
        blank = True, 
        upload_to = 'galeria',
        sizes=((125,125),(200,200),(500,500))
    )
    dataPublicacao = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        #return reverse('album', kwargs={'slug': self.slug})
        return self.original
    
    def get_exibicao(self):
        nome_arq = str(self.original)
        delimiter = nome_arq.find(".JPG")
        nome_arq = nome_arq[:delimiter] + ".500x500.jpg"
        return nome_arq
    
    def get_thumbnail(self):
        nome_arq = str(self.original)
        delimiter = nome_arq.find(".JPG")
        nome_arq = nome_arq[:delimiter] + ".125x125.jpg"
        return nome_arq
        
    class Meta: 
        ordering =('album', 'titulo',)
        db_table = 'psssv_fotos'

class AlbumUpload(models.Model):
    zip = models.FileField(_('images file (.zip)'), upload_to="/temp",
                                help_text=_('Select a .zip file of images to upload into a new Gallery.'))
    album = models.ForeignKey(Album, null=True, blank=True, help_text=_('Select a gallery to add these videos to. leave this empty to create a new gallery from the supplied title.'))
    titulo = models.CharField(_('title'), max_length=75, help_text=_('All videos in the gallery will be given a title made up of the gallery title + a sequential number.'))
    descricao = models.TextField(_('description'), blank=True, help_text=_('Descricao dessa galeria.'))
    data = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = _('album upload')
        verbose_name_plural = _('album uploads')

    def save(self, *args, **kwargs):
        super(AlbumUpload, self).save(*args, **kwargs)
        album = self.process_zipfile()
        super(AlbumUpload, self).delete()
        return album

    def process_zipfile(self):
        if os.path.isfile(self.zip_file.path):
            # TODO: implement try-except here
            zip = zipfile.ZipFile(self.zip_file.path)
            bad_file = zip.testzip()
            if bad_file:
                raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)
            count = 1
            if self.album:
                Album = self.Album
            else:
                album = Album.objects.create(titulo=self.titulo,
                                                 slug=slugify(self.titulo),
                                                 data=self.data,
                                                 )
            from cStringIO import StringIO
            for filename in zip.namelist():
                if filename.startswith('__'): # do not process meta files
                    continue
                data = zip.read(filename)
                if len(data):
                    while 1:
                        titulo = ' '.join([self.titulo, str(count)])
                        slug = slugify(titulo)
                        try:
                            p = Foto.objects.get(titulo_slug=slug)
                        except Foto.DoesNotExist:
                            foto = Foto(titulo=titulo,
                                          slug=slug,
                                          caption=self.caption,
                                          descricao =self.descricao ,
                                         )
                            foto.save(filename, ContentFile(data), save=False)
                            foto.save()
                            album.add(foto)
                            count = count + 1
                            break
                        count = count + 1
            zip.close()
            return album
       

        
#Signals
from django.db.models import signals
from utils.signals_comuns import slug_pre_save
signals.pre_save.connect(slug_pre_save, sender = Album)
signals.pre_save.connect(slug_pre_save, sender = Foto)    