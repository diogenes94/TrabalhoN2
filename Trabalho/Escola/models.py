#coding:utf-8
from django.db import models

class Curso(models.Model):
	Nome = models.CharField('Nome do Curso',max_length=100,null=True)

class Estrutura(models.Model):
	Curso = models.ForeignKey(Curso,verbose_name='Curso')

class Periodo (models.Model):
	Periodo = models.CharField('Período')

class Disciplina (models.Model):

class DisciplinaPeriodo(models.Model):

class Turma(models.Model):

class Semestre(models.Model):

class TurmaDisciplina(models.Model):

class Aluno(models.Model):

class TurmaAluno(models.Model):

class DisciplinaAluno(models.Model):

class TurmaDiscplinaHorario(models.Model):

class Professor(models.Model):

class Horario(models.Model):


# Create your models here.
