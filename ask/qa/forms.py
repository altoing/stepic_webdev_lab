# -*- coding: utf-8 -*-

from django import forms
from models import Question,Answer

class AskForm (forms.Form):
    title = forms.CharField(label=u'Заголовок')
    text = forms.CharField(label=u'Вопрос', widget=forms.Textarea)

class AnswerForm (forms.Form):
    text = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput())