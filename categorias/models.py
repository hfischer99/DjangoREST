from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=255, unique=True, verbose_name="Nome")
