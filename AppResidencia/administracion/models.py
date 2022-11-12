from django.db import models

# Create your models here.

class Residencia(models.Model):
    calle = models.CharField(max_length=20)
    numero = models.CharField(max_length=10)
    fono = models.CharField(max_length=8)
    propietario = models.CharField(max_length=40)
    def save(self, force_insert=False, force_update=False):
        self.calle = self.calle.upper()
        self.propietario = self.propietario.upper()
        super(Residencia, self).save(force_insert, force_update)
        

class Correspondencia(models.Model):
    residencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)
    TIPOS = models.TextChoices('TIPOS', 'DOCUMENTO ENCOMIENDA')
    ESTADOS = models.TextChoices('ESTADOS', 'PENDIENTE ENTREGADO')
    tipo = models.CharField(choices = TIPOS.choices, max_length=10)
    estado = models.CharField(choices = ESTADOS.choices, max_length=10)
    fecha_recepcion = models.DateField()