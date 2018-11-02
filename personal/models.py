# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Project(models.Model):
    """Model for storing information about my projects. Posts will be
    presented on the main page in sequence"""
    def __str__(self):
        """String representation of an model"""
        return self.title

    title = models.CharField(max_length=100)
    overview = models.TextField()
    cover = models.FileField(blank=True)
    link = models.URLField(blank=True)
    posted = models.DateField(auto_now=True)

