from django.db import models
from django.conf import settings
from django.utils import timezone,timesince
# Create your models here.



class Posteo(models.Model):
    auto = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
  
    def publicado(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo