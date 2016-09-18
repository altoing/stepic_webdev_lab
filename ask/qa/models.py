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
    def new():
        pass
    def popular():
        pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.CharField(max_length=255)
    likes = models.TextField()

class Answers(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(User)


