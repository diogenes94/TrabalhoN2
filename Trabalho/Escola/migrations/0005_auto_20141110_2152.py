# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escola', '0004_auto_20141110_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='Nome',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Turma'),
        ),
    ]
