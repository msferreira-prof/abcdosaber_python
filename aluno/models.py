from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70, help_text='Informe o nome do aluno')
    data_inicial = models.DateField(null=True, blank=True, help_text='Informe a data inicial de matrícula do aluno')
    data_final = models.DateField(null=True, blank=True, help_text='Informe a data de final de matrícula do aluno')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['matricula']
    
    def __str__(self):
        return f'{self.matricula} - {self.nome}'
