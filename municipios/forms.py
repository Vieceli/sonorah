# -*- coding: utf-8 -*-
from django import forms
from widgets import SelectMunicipioWidget

class FormMunicipio(forms.Form):
    #municipio = forms.IntegerField(label=u"Estado - Cidade", widget=SelectMunicipioWidget, required=False)
    municipio = forms.IntegerField(widget=SelectMunicipioWidget, required=False)