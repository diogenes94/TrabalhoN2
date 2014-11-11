# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('CPF', models.CharField(max_length=14, unique=True, null=True, verbose_name=b'CPF')),
                ('DataNascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Telefone', models.CharField(max_length=15, null=True, verbose_name=b'Telefone')),
                ('Celular', models.CharField(max_length=15, null=True, verbose_name=b'Celular')),
                ('Email', models.EmailField(max_length=100, verbose_name=b'Endere\xc3\xa7o de email', blank=True)),
                ('Logradouro', models.CharField(max_length=100, null=True, verbose_name=b'Logradouro')),
                ('Numero', models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero')),
                ('Complemento', models.CharField(max_length=100, null=True, verbose_name=b'Complemento', blank=True)),
                ('Bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('Cidade', models.CharField(max_length=100, null=True, verbose_name=b'Cidade')),
                ('UF', models.CharField(max_length=2, null=True, verbose_name=b'UF', choices=[(b'AC', b'Acre - AC'), (b'AL', b'Alagoas - AL'), (b'AP', b'Amap\xc3\xa1 - AP'), (b'AM', b'Amazonas - AM'), (b'BA', b'Bahia - BA'), (b'CE', b'Cear\xc3\xa1 - CE'), (b'DF', b'Distrito Federal - DF'), (b'ES', b'Esp\xc3\xadrito Santo - ES'), (b'GO', b'Goi\xc3\xa1s - GO'), (b'MA', b'Maranh\xc3\xa3o - MA'), (b'MT', b'Mato Grosso - MT'), (b'MS', b'Mato Grosso do Sul - MS'), (b'MG', b'Minas Gerais - MG'), (b'PA', b'Par\xc3\xa1 - PA'), (b'PB', b'Para\xc3\xadba - PB'), (b'PR', b'Paran\xc3\xa1 - PR'), (b'PE', b'Pernambuco - PE'), (b'PI', b'Piau\xc3\xad - PI'), (b'RJ', b'Rio de Janeiro - RJ'), (b'RN', b'Rio Grande do Norte - RN'), (b'RS', b'Rio Grande do Sul - RS'), (b'RO', b'Rond\xc3\xb4nia - RO'), (b'RR', b'Roraima - RR'), (b'SC', b'Santa Catarina - SC'), (b'SP', b'S\xc3\xa3o Paulo - SP'), (b'SE', b'Sergipe - SE'), (b'TO', b'Tocantins - TO')])),
                ('CEP', models.CharField(max_length=9, null=True, verbose_name=b'CEP')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Curso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=50, null=True, verbose_name=b'Nome da Disciplina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisciplinaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estrutura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=50, null=True, verbose_name=b'Nome da Estrutura')),
                ('Curso', models.ForeignKey(verbose_name=b'Curso', to='Escola.Curso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstruturaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Disciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Escola.Disciplina')),
                ('Estrutura', models.ForeignKey(verbose_name=b'Estrutura', to='Escola.Estrutura')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HoraInicio', models.TimeField(verbose_name=b'Hor\xc3\xa1rio de Inicio')),
                ('HoraFim', models.TimeField(verbose_name=b'Hor\xc3\xa1rio de Inicio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Periodo', models.CharField(max_length=3, verbose_name=b'Per\xc3\xadodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('CPF', models.CharField(max_length=14, unique=True, null=True, verbose_name=b'CPF')),
                ('DataNascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Telefone', models.CharField(max_length=15, null=True, verbose_name=b'Telefone')),
                ('Celular', models.CharField(max_length=15, null=True, verbose_name=b'Celular')),
                ('Email', models.EmailField(max_length=100, verbose_name=b'Endere\xc3\xa7o de email', blank=True)),
                ('Logradouro', models.CharField(max_length=100, null=True, verbose_name=b'Logradouro')),
                ('Numero', models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero')),
                ('Complemento', models.CharField(max_length=100, null=True, verbose_name=b'Complemento', blank=True)),
                ('Bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('Cidade', models.CharField(max_length=100, null=True, verbose_name=b'Cidade')),
                ('UF', models.CharField(max_length=2, null=True, verbose_name=b'UF', choices=[(b'AC', b'Acre - AC'), (b'AL', b'Alagoas - AL'), (b'AP', b'Amap\xc3\xa1 - AP'), (b'AM', b'Amazonas - AM'), (b'BA', b'Bahia - BA'), (b'CE', b'Cear\xc3\xa1 - CE'), (b'DF', b'Distrito Federal - DF'), (b'ES', b'Esp\xc3\xadrito Santo - ES'), (b'GO', b'Goi\xc3\xa1s - GO'), (b'MA', b'Maranh\xc3\xa3o - MA'), (b'MT', b'Mato Grosso - MT'), (b'MS', b'Mato Grosso do Sul - MS'), (b'MG', b'Minas Gerais - MG'), (b'PA', b'Par\xc3\xa1 - PA'), (b'PB', b'Para\xc3\xadba - PB'), (b'PR', b'Paran\xc3\xa1 - PR'), (b'PE', b'Pernambuco - PE'), (b'PI', b'Piau\xc3\xad - PI'), (b'RJ', b'Rio de Janeiro - RJ'), (b'RN', b'Rio Grande do Norte - RN'), (b'RS', b'Rio Grande do Sul - RS'), (b'RO', b'Rond\xc3\xb4nia - RO'), (b'RR', b'Roraima - RR'), (b'SC', b'Santa Catarina - SC'), (b'SP', b'S\xc3\xa3o Paulo - SP'), (b'SE', b'Sergipe - SE'), (b'TO', b'Tocantins - TO')])),
                ('CEP', models.CharField(max_length=9, null=True, verbose_name=b'CEP')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=6, null=True, verbose_name=b'Semestre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=6, null=True, verbose_name=b'Turma')),
                ('Semestre', models.ForeignKey(verbose_name=b'Turma', to='Escola.Semestre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Aluno', models.ForeignKey(verbose_name=b'Aluno', to='Escola.Aluno')),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='Escola.Turma')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Disciplina', models.ForeignKey(verbose_name=b'Disciplina', to='Escola.Disciplina')),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='Escola.Turma')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaDiscplinaHorario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Horario', models.ForeignKey(verbose_name=b'Horario', to='Escola.Horario')),
                ('Professor', models.ForeignKey(verbose_name=b'Professor', to='Escola.Professor')),
                ('TurmaDisciplina', models.ForeignKey(verbose_name=b'Turma Disciplina', to='Escola.TurmaDisciplina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estruturadisciplina',
            name='Periodo',
            field=models.ForeignKey(verbose_name=b'Per\xc3\xadodo', to='Escola.Periodo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplinaaluno',
            name='Aluno',
            field=models.ForeignKey(verbose_name=b'Aluno', to='Escola.TurmaAluno'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplinaaluno',
            name='Disciplina',
            field=models.ForeignKey(verbose_name=b'Disciplina', to='Escola.TurmaDisciplina'),
            preserve_default=True,
        ),
    ]
