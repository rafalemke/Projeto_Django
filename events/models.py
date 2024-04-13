from django.db import models

# Create your models here.

class Evento(models.Model):
    CHOICES = [('P', 'Pendente'),
               ('A', 'Em andamento'),
               ('C', 'Concluido')]
    
    nome = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.TextField()
    status = models.CharField(max_length=1, choices=CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add= True)

    
    


    def __str__(self):
        return self.nome
