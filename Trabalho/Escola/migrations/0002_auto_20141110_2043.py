# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escola', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='Nome',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Turma'),
        ),
    ]
