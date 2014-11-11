# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escola', '0003_turma_estrutura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmadisciplina',
            name='Disciplina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='Escola.EstruturaDisciplina'),
        ),
    ]
