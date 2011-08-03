# -*- coding: utf-8 -*- 
'''
Created on 29/04/2011

@author: jhoni
'''
from django import forms
from django.template.defaultfilters import filesizeformat

""" 
BR-specific Form helpers 
""" 
   
from django.forms import ValidationError 
from django.forms.fields import Field, RegexField, CharField, Select, EMPTY_VALUES , FileField
from django.utils.encoding import smart_unicode 
from django.utils.translation import ugettext_lazy as _ 
import re 
   
try: 
   set 
except NameError: 
   from sets import Set as set     # For Python 2.3 
  
phone_digits_re = re.compile(r'^(\d{2})[-\.]?(\d{4})[-\.]?(\d{4})$') 

class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):        
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        
        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('Filetype not supported.'))
        except AttributeError:
            pass        
            
        return data


class TelefoneField(CharField):
    default_error_messages = { 
                              'invalid': _('Phone numbers must be in XX-XXXX-XXXX format.'), 
                            }
    def clean(self, value):
        super(TelefoneField, self).clean(value) 
        if value in EMPTY_VALUES: 
            return u'' 
        value = re.sub('(\(|\)|\s+)', '', smart_unicode(value))
        m = phone_digits_re.search(value)
        if m:
            return u'%s-%s-%s' % (m.group(1), m.group(2), m.group(3))
        raise ValidationError(self.error_messages['invalid'])
    

def DV_maker(v):
    if v >= 2: 
        return 11 - v 
    return 0
 
class CPFField(CharField):
    """ 87 This field validate a CPF number or a CPF string. A CPF number is 88 compounded by XXX.XXX.XXX-VD. The two last digits are check digits. 89 90 More information: 91 http://en.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas 92 """ 
    default_error_messages = { 
                              'invalid': _("Invalid CPF number."), 
                              'max_digits': _("This field requires at most 11 digits or 14 characters."), 
                              'digits_only': _("This field requires only numbers."), 
                              } 
    def __init__(self, *args, **kwargs):
        super(CPFField, self).__init__(max_length=14, min_length=11, *args, **kwargs)

    def clean(self, value):
        """ 104 Value can be either a string in the format XXX.XXX.XXX-XX or an 105 11-digit number. 106 """ 
        value = super(CPFField, self).clean(value)
        if value in EMPTY_VALUES: 
            return u'' 
        orig_value = value[:] 
        if not value.isdigit(): 
            value = re.sub("[-\.]", "", value) 
        try: 
            int(value) 
        except ValueError: 
            raise ValidationError(self.error_messages['digits_only']) 
        if len(value) != 11: 
            raise ValidationError(self.error_messages['max_digits']) 
        orig_dv = value[-2:] 
        
        new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))]) 
        new_1dv = DV_maker(new_1dv % 11) 
        value = value[:-2] + str(new_1dv) + value[-1] 
        new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))]) 
        new_2dv = DV_maker(new_2dv % 11) 
        value = value[:-1] + str(new_2dv) 
        if value[-2:] != orig_dv: 
            raise ValidationError(self.error_messages['invalid']) 
        
        return orig_value


#
#132 -class BRCNPJField(Field):
#133 default_error_messages = { 134 'invalid': _("Invalid CNPJ number."), 135 'digits_only': _("This field requires only numbers."), 136 'max_digits': _("This field requires at least 14 digits"), 137 } 138
#139 - def clean(self, value):
#140 """ 141 Value can be either a string in the format XX.XXX.XXX/XXXX-XX or a 142 group of 14 characters. 143 """ 144 value = super(BRCNPJField, self).clean(value) 145 if value in EMPTY_VALUES: 146 return u'' 147 orig_value = value[:] 148 if not value.isdigit(): 149 value = re.sub("[-/\.]", "", value) 150 try: 151 int(value) 152 except ValueError: 153 raise ValidationError(self.error_messages['digits_only']) 154 if len(value) != 14: 155 raise ValidationError(self.error_messages['max_digits']) 156 orig_dv = value[-2:] 157 158 new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(5, 1, -1) + range(9, 1, -1))]) 159 new_1dv = DV_maker(new_1dv % 11) 160 value = value[:-2] + str(new_1dv) + value[-1] 161 new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(6, 1, -1) + range(9, 1, -1))]) 162 new_2dv = DV_maker(new_2dv % 11) 163 value = value[:-1] + str(new_2dv) 164 if value[-2:] != orig_dv: 165 raise ValidationError(self.error_messages['invalid']) 166 167 return orig_value
#168   
#class BRZipCodeField(RegexField):
#20 default_error_messages = { 21 'invalid': _('Enter a zip code in the format XXXXX-XXX.'), 22 } 23
#24 - def __init__(self, *args, **kwargs):
#25 super(BRZipCodeField, self).__init__(r'^\d{5}-\d{3}$', 26 max_length=None, min_length=None, *args, **kwargs)
# 27   
#43 -class BRStateSelect(Select):
#44 """ 45 A Select widget that uses a list of Brazilian states/territories 46 as its choices. 47 """
#48 - def __init__(self, attrs=None):
#49 from br_states import STATE_CHOICES 50 super(BRStateSelect, self).__init__(attrs, choices=STATE_CHOICES)
# 51   
#52 -class BRStateChoiceField(Field):
#53 """ 54 A choice field that uses a list of Brazilian states as its choices. 55 """ 56 widget = Select 57 default_error_messages = { 58 'invalid': _(u'Select a valid brazilian state. That state is not one of the available states.'), 59 } 60
#61 - def __init__(self, required=True, widget=None, label=None, 62 initial=None, help_text=None):
#63 super(BRStateChoiceField, self).__init__(required, widget, label, 64 initial, help_text) 65 from br_states import STATE_CHOICES 66 self.widget.choices = STATE_CHOICES
#67
#68 - def clean(self, value):
#69 value = super(BRStateChoiceField, self).clean(value) 70 if value in EMPTY_VALUES: 71 value = u'' 72 value = smart_unicode(value) 73 if value == u'': 74 return value 75 valid_values = set([smart_unicode(k) for k, v in self.widget.choices]) 76 if value not in valid_values: 77 raise ValidationError(self.error_messages['invalid']) 78 return value
# 79   
