from django.contrib import admin

from .models import Cliente, Reserva, Sala, Sede

admin.site.register([Sede, Sala, Cliente, Reserva])
