# -*- coding: utf-8 -*-
'''
Created on 03/05/2011

@author: jhoni
'''

#from django import forms
#from principal.models import Cadastra_Email
from django.forms.models import ModelForm
from artistas.models import Artista_Contato


class ArtistaForm(ModelForm):
    class Meta:
        model = Artista_Contato


#class NoticiaAdminForm(ModelForm):
#    class Meta:
#        model = Noticia
#        fields = ('titulo', 'subtitulo', 'slug','miniatura','texto','resumo')
#        widgets = {
#            'resumo': Textarea(attrs={'cols': 80, 'rows': 20}),
#        }

#class FormBuscar(forms.Form):
#    query = forms.CharField(label=u'Procurar por: ',widget=forms.TextInput(attrs={'size': 32}))
#    
#
#
#class FormCadEmail(forms.Form):
#    email = forms.EmailField(label=u'Digite o email: ',widget=forms.TextInput(attrs={'size': 32}))
#    remover = forms.BooleanField(label=u'Remover e-mail', widget=forms.CheckboxInput())
#    
#    
#    def clean_email(self):
#        email = self.cleaned_data['email']
#        try:
#            Cadastra_Email.objects.get(email=email)
#        except Cadastra_Email.DoesNotExist:
#            return email
#        raise forms.ValidationError('Email ja cadastrado')     