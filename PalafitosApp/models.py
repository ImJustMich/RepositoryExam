from django.db import models

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    fecha_viaje = models.DateField()
    metodoPago = models.CharField(max_length=100, choices=[
        ('credito', 'credito'),
        ('debito', 'debito'),
        ('paypal', 'paypal'),
        ('transferencia', 'transferencia')
        ], default='debito')
    categoria = models.CharField(max_length=100, choices=[
        ('primeraClase', 'primeraClase'),
        ('claseEjecutiva', 'claseEjecutiva'),
        ('economicaPremium', 'economicaPremium'),
        ('economica', 'economica')
        ], default='economica')


class Donacion(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    monto = models.CharField(max_length=999)

