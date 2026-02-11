from django.db import models

# Create your models here.
class Titulo(models.Model):
    codigo = models.AutoField(primary_key=True, 
                                help_text="Código do Título")
    descricao = models.TextField(max_length=70, 
                                 null=False, 
                                 help_text="Informe a descrição do Título")

    def __str__(self):
        return self.nome