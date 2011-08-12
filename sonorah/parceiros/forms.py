'''
Created on 20/07/2011

@author: jhoni
'''
from parceiros.models import Contratante, Compositor, Radialista, Parceiro
from django.forms.models import ModelForm

class ContratantesForm(ModelForm):
        #nome = forms.CharField(label='Seu Nome',required=True,initial="Seu Nome",help_text='Digite seu nome corretamente', error_messages={'required': 'Por Favor coloque seu Nome'})
    class Meta:
        model = Contratante

class CompositoresForm(ModelForm):
    class Meta:
        model = Compositor

class RadialistaForm(ModelForm):
    class Meta:
        model = Radialista
        
class ParceiroForm(ModelForm):
    class Meta:
        model = Parceiro