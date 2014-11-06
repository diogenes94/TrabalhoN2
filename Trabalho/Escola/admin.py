from django.contrib import admin
from models import Curso,Estrutura,Periodo,Disciplina,EstruturaDisciplina,Turma,Semestre,TurmaDisciplina
from models import Aluno,TurmaAluno,DisciplinaAluno,TurmaDiscplinaHorario,ProfessorProfessor,Horario

class CursoAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
		
# Register your models here.
admin.site.register(Curso,CursoAdmin)