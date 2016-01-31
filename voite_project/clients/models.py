# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
    """
    models clients for voition
    """
    name = models.CharField(max_length=100, verbose_name=u'Имя')
    surname = models.CharField(max_length=250, verbose_name=u'Фамилия')
    age = models.IntegerField(verbose_name=u'Возраст')
    birthday = models.DateField(verbose_name=u'Дата')
    photo = models.ImageField(max_length=250, upload_to='photo',
                              null=True, verbose_name=u'Фото')
    voite = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def save(self):
        if self.voite > 10:
            self.voite = 10
        super(Client, self).save()

    def __getitem__(self, attrname):
        return self.__getattribute__(attrname)

    def __str__(self):
        return self.surname

    def unicode(self):
        return self.surname
