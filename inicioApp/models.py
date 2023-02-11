from django.db import models

# Create your models here.
class Trabajador(models.Model):
    id = models.IntegerField(primary_key=True)
    ci = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fcha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    estado = models.IntegerField()
    class Meta: db_table = 'trabajador'

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    id_trabajador= models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    estado = models.IntegerField()
    class Meta: db_table = 'usuario'





