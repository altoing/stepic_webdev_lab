# -*- coding: utf-8 -*-

from django import forms

class AskForm (forms.Form):
    title = forms.CharField(label=u'Заголовок')
    text = forms.CharField(label=u'Вопрос', widget=forms.Textarea)

class AnswerForm (forms.Form):
    text = forms.CharField(widget=forms.Textarea)