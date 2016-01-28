# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f')),
                ('surname', models.CharField(max_length=250, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('age', models.IntegerField(verbose_name='\u0412\u043e\u0437\u0440\u0430\u0441\u0442')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('photo', models.ImageField(max_length=250, null=True, verbose_name='\u0424\u043e\u0442\u043e', upload_to='photo')),
                ('voite', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
