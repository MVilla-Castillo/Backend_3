from django.db import models


class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre


class Sala(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='salas')
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    precio_hora = models.DecimalField(max_digits=10, decimal_places=2)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} - {self.sede}'


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    empresa = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cliente} - {self.sala} - {self.fecha}'
