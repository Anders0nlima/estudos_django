from django.db import models

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome  
