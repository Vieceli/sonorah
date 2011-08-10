'''
Created on 02/08/2011

@author: Jhoni

'''

# -*- coding: utf-8
try:
    import Image
except ImportError:
    from PIL import Image
import os

from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.template import Library
from galeria.models import Foto,Album

register = Library()

class adminAlbum(admin.ModelAdmin):
    list_display = ('titulo','deletar')
    search_fields = ('titulo',)
    prepopulated_fields = {"slug": ("titulo",)}
    
    def deletar(self,object):
        return '<a href=/admin/galeria/album/%s/delete/>Deletar<a/>' %(object.id)
    deletar.allow_tags = True
    
class FormFoto(forms.ModelForm):
    class Meta: 
        model = Foto
     
class adminFoto(admin.ModelAdmin):
    list_display = ('album', 'titulo', 'slug', 'deletar')
    list_filter = ['album']
    prepopulated_fields = {"slug": ("titulo",)}
    search_fields = ('titulo', 'descricao',)
    form = FormFoto
    
    def deletar(self,object):
        return '<a href=/admin/galeria/foto/%s/delete/>Deletar<a/>' %(object.id)
    deletar.allow_tags = True
    
    def save(self, request, obj, form, change):
        """ Metodo para criar as miniaturas... """
        super(adminFoto, self).save_model(request, obj, form, change)
        obj.save()

admin.site.register(Album, adminAlbum)
admin.site.register(Foto, adminFoto)
