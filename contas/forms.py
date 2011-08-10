# -*- coding: utf-8 -*-
'''
Created on 13/07/2011

@author: Jhoni
'''
from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail

class LoginForm(forms.Form):
    usuario = forms.CharField(label=u'Email ou Usuario')
    senha = forms.CharField(widget=forms.PasswordInput(),max_length=100)


class FormularioRegistro(forms.ModelForm):       
    senha1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    senha2 = forms.CharField(label=u"Confirmação de senha", widget=forms.PasswordInput,
                                help_text = "Repita sua senha.")
    email1 = forms.EmailField(label="Email", max_length=75)
    email2 = forms.EmailField(label="Confirme seu e-mail", max_length=75,
                              help_text = u"Entre com seu endereço de e-mail novamente.")

    class Meta:
        model = User
        fields = ("username",)
        
    def clean_senha2(self):
        if 'senha1' in self.cleaned_data:
            senha1 = self.cleaned_data['senha1']
            senha2 = self.cleaned_data['senha2']
            if senha1 == senha2:
                return senha2
        raise forms.ValidationError(u'As senhas não são iquais.')
  
    def clean_email1(self):
        email = self.cleaned_data['email1']
        try:
            User.objects.get(username=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(u'Usuário ja cadastrado')
      
    def clean_email2(self):
        email1 = self.cleaned_data.get("email1", "")
        email2 = self.cleaned_data["email2"]
        if email1 != email2:
            raise forms.ValidationError(u'Os e-mails não são iquais.')
        return email2
    
    def envia_email(self):
        #usuario = self.cleaned_data['username']
        senha = self.cleaned_data['senha1']
        email = self.cleaned_data['email']
        titulo = u'Mensagem enviada pelo site na criacao do usuario'
        destino = 'veiodruida@gmail.com'
        texto = u"Bem vindo:" + email +"\nSua Senha: "+ senha + "\nSeu email: "+email + "\n"
        
        #texto nao esta correto quando chega na caixa de email
        if titulo and texto and destino:
            try:
                send_mail(
                    subject=titulo,
                    message=texto,
                    from_email=destino,#mudar destino posteriormente
                    recipient_list=[destino],
                    fail_silently=False
                    )
            except Exception, e:
                print("Erro")
                print e