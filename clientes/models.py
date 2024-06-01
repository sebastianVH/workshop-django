from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'