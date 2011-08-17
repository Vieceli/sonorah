# -*- coding: utf-8 -*-
'''
Created on 20/07/2011

@author: jhoni
'''
from parceiros.models import Contratante, Compositor, Radialista, Parceiro
from django.forms.models import ModelForm
from django import forms
from municipios.widgets import SelectMunicipioWidget

class ContratantesForm(ModelForm):
    cidade = forms.IntegerField( widget=SelectMunicipioWidget)  
        #nome = forms.CharField(label='Seu Nome',required=True,initial="Seu Nome",help_text='Digite seu nome corretamente', error_messages={'required': 'Por Favor coloque seu Nome'})
    class Meta:
        model = Contratante

class CompositoresForm(ModelForm):
    class Meta:
        model = Compositor

class RadialistaForm(ModelForm):
    cidade = forms.IntegerField( widget=SelectMunicipioWidget)  
    class Meta:
        model = Radialista
        
class ParceiroForm(ModelForm):
#class ParceiroForm(forms.Form):
    cidade = forms.IntegerField( widget=SelectMunicipioWidget)    
    class Meta:
        model = Parceiro