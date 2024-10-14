from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'email', 'registration_number', 'crated_at', 'modified_at')
    search_fields = ('nome', 'email', 'registration_number')
