from django.contrib import admin
from models import Curso,Estrutura,Periodo,Disciplina,EstruturaDisciplina,Turma,Semestre,TurmaDisciplina
from models import Aluno,TurmaAluno,DisciplinaAluno,TurmaDiscplinaHorario,Professor,Horario

class EstruturaDisciplinaInline(admin.TabularInline):
	model = EstruturaDisciplina

class TurmaAlunoInline(admin.TabularInline):
	model = TurmaAluno

class CursoAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

class EstruturaAdmin(admin.ModelAdmin):
	list_filter = ['Curso','Nome']
	list_display = ['Curso','Nome']
	search_fields = ['Curso','Nome']
	inlines = [EstruturaDisciplinaInline]
	save_as = True

class PeriodoAdmin(admin.ModelAdmin):
	list_display = ['Periodo']
	list_filter = ['Periodo']
	search_fields =['Periodo']
	save_as = True

class DisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

class TurmaAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	inlines = [TurmaAlunoInline]	
	save_as = True

class SemestreAdmin(admin.ModelAdmin):
	list_filter = ['Nome']
	list_display = ['Nome']
	search_fields = ['Nome']
	save_as = True
class TurmaDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Turma','Disciplina']
	list_filter = ['Turma','Disciplina']
	search_fields = ['Turma','Disciplina']
	save_as = True

class AlunoAdmin(admin.ModelAdmin):
	list_display = ['Nome','CPF','Sexo','DataNascimento']
	list_filter = ['Nome','CPF']
	search_fields = ['Nome','CPF']
	save_as = True

class DisciplinaAlunoAdmin(admin.ModelAdmin):
	list_display = ['Disciplina','Aluno']
	list_filter = ['Disciplina','Aluno']
	search_fields = ['Disciplina','Aluno']
	save_as = True

class ProfessorAdmin(admin.ModelAdmin):
	list_display = ['Nome','CPF','Sexo','DataNascimento']
	list_filter = ['Nome','CPF']
	search_fields = ['Nome','CPF']
	save_as = True

class HorarioAdmin(admin.ModelAdmin):
	list_filter = ['HoraInicio','HoraFim'] 
	list_display = ['HoraInicio','HoraFim'] 
	search_fields = ['HoraInicio','HoraFim'] 
	save_as = True

class TurmaDiscplinaHorarioAdmin(admin.ModelAdmin):
	list_display = ['Professor','TurmaDisciplina','Horario']
	list_filter = ['Professor','TurmaDisciplina','Horario']
	search_fields = ['Professor','TurmaDisciplina','Horario']
	save_as = True
# Register your models here.
admin.site.register(Curso,CursoAdmin)
admin.site.register(Estrutura,EstruturaAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Turma,TurmaAdmin)
admin.site.register(Semestre,SemestreAdmin)
admin.site.register(TurmaDisciplina,TurmaDisciplinaAdmin)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(DisciplinaAluno,DisciplinaAlunoAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Horario,HorarioAdmin)
admin.site.register(TurmaDiscplinaHorario,TurmaDiscplinaHorarioAdmin)