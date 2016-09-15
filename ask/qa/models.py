# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=60)

    # Так в админке будит username вместо фигни
    def __unicode__(self):
        return self.username