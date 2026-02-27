from django.db import models

from titulo.models import Titulo

# Create your models here.
class Instrutor(models.Model):
    id = models.AutoField(primary_key=True)
    rg = models.CharField(max_length=15,  help_text='Informe o RG do instrutor')
    nome = models.CharField(max_length=70, help_text='Informe o nome do instrutor')
    data_nascimento = models.DateField(null=True, blank=True, help_text='Informe a data de nascimento do instrutor')
    telefone = models.CharField(max_length=9, help_text='Informe o telefone do instrutor')
    ddd = models.CharField(max_length=3, help_text='Informe o DDD do telefone do instrutor')
    codigo_titulo = models.ForeignKey(Titulo, null=True, blank=True, related_name='titulos', 
                                       on_delete=models.SET_NULL, 
                                       db_column='codigo_titulo', 
                                       help_text='Informe o título do instrutor')

    class Meta:
        verbose_name = 'Instrutor'
        verbose_name_plural = 'Instrutores'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.id} - {self.nome}'
