#coding:utf-8
from django.db import models

SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')

]

ESTADO_OPCOES = [
 ('AC','Acre - AC'),
 ('AL','Alagoas - AL'),
 ('AP','Amapá - AP'),
 ('AM','Amazonas - AM'),
 ('BA','Bahia - BA'),
 ('CE','Ceará - CE'),
 ('DF','Distrito Federal - DF'),
 ('ES','Espírito Santo - ES'),
 ('GO','Goiás - GO'),
 ('MA','Maranhão - MA'),
 ('MT','Mato Grosso - MT'),
 ('MS','Mato Grosso do Sul - MS'),
 ('MG','Minas Gerais - MG'),
 ('PA','Pará - PA'),
 ('PB','Paraíba - PB'),
 ('PR','Paraná - PR'),
 ('PE','Pernambuco - PE'),
 ('PI','Piauí - PI'),
 ('RJ','Rio de Janeiro - RJ'),
 ('RN','Rio Grande do Norte - RN'),
 ('RS','Rio Grande do Sul - RS'),
 ('RO','Rondônia - RO'),
 ('RR','Roraima - RR'),
 ('SC','Santa Catarina - SC'),
 ('SP','São Paulo - SP'),
 ('SE','Sergipe - SE'),
 ('TO','Tocantins - TO')
]

class Semestre(models.Model):
	Nome = models.CharField('Semestre',max_length=6,null=True)
	
	def __unicode__(self):
		return self.Nome


class Curso(models.Model):
	Nome = models.CharField('Nome do Curso',max_length=100,null=True)

	def __unicode__(self):
		return self.Nome


class Estrutura(models.Model):
	Curso = models.ForeignKey(Curso,verbose_name='Curso')
	Nome = models.CharField('Nome da Estrutura',max_length=50,null=True)

	def __unicode__(self):
		return self.Curso.Nome


class Periodo (models.Model):
	Periodo = models.CharField('Período',max_length=3)

	def __unicode__(self):
		return self.Periodo


class Disciplina (models.Model):
	Nome = models.CharField('Nome da Disciplina',max_length=50,null=True)
	def __unicode__(self):
		return self.Nome

class EstruturaDisciplina(models.Model):
	Estrutura = models.ForeignKey(Estrutura,verbose_name='Estrutura')
	Periodo = models.ForeignKey(Periodo,verbose_name='Período')
	Disciplina = models.ForeignKey(Disciplina,verbose_name='Disciplina')

	def __unicode__(self):
		return "%s - %s" % (self.Estrutura.Nome,self.Periodo.Nome)


class Turma(models.Model):
	Semestre = models.ForeignKey(Semestre,verbose_name='Turma')
	Nome = models.CharField('Turma',max_length=6,null=True)

	def __unicode__(self):
		return "%s - %s" % (self.Semestre.Nome,self.Nome)




class TurmaDisciplina(models.Model):
	Turma = models.ForeignKey(Turma,verbose_name='Turma')
	Disciplina = models.ForeignKey(Disciplina,verbose_name='Disciplina')

	def __unicode__(self):
		return "%s - %s" % (self.Turma.Nome,self.Disciplina)



class Aluno(models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=14,unique=True,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100,blank=True)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	UF = models.CharField('UF', max_length=2,choices=ESTADO_OPCOES,null=True)
 	CEP = models.CharField('CEP', max_length=9,null=True)	
 	
 	def __unicode__(self):
		return self.Nome

class TurmaAluno(models.Model):
	Turma = models.ForeignKey(Turma,verbose_name='Turma')
	Aluno = models.ForeignKey(Aluno,verbose_name='Aluno')

	def __unicode__(self):
		return "%s - %s" % (self.Turma.Nome,self.Aluno.Nome)



class DisciplinaAluno(models.Model):
	Disciplina = models.ForeignKey(TurmaDisciplina,verbose_name='Disciplina')
	Aluno = models.ForeignKey(TurmaAluno,verbose_name='Aluno')

	def __unicode__(self):
		return "%s - %s" % (self.Disciplina.Disciplina.Nome,self.Aluno.Nome)

class TurmaDiscplinaHorario(models.Model):
	Professor = models.ForeignKey(Professor,verbose_name='Professor')
	TurmaDisciplina = models.ForeignKey(TurmaDisciplina,verbose_name='Turma Disciplina')
	Horario = models.ForeignKey(Horario,verbose_name='Horario')

	def __unicode__(self):
		return "%s - %s - %s" % (self.TurmaDisciplina.Disciplina.Nome,self.Professor.Nome,self.Horario)


class Professor(models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=14,unique=True,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100,blank=True)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	UF = models.CharField('UF', max_length=2,choices=ESTADO_OPCOES,null=True)
 	CEP = models.CharField('CEP', max_length=9,null=True)

 	def __unicode__(self):
		return self.Nome

class Horario(models.Model):
	HoraInicio = models.TimeField('Horário de Inicio')
	HoraFim = models.TimeField('Horário de Inicio')
	def __unicode__(self):
		return "%s - %s" % (self.HoraInicio,self.HoraFim)


# Create your models here.
