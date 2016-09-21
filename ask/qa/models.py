# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=60)

    # Так в админке будит username вместо фигни
    def __unicode__(self):
        return self.username

class QuestionManager(models.Manager):
    def new(self):
        return super (QuestionManager, self).get_queryset().order_by("-added_at")
    def popular(self):
        return super (QuestionManager, self).get_queryset().order_by("-rating")

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='+')
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.question.title

