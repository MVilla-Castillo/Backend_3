from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Cliente, Reserva, Sala, Sede
from .serializers import ClienteSerializer, ReservaSerializer, SalaSerializer, SedeSerializer


def index(request):
    return render(request, 'cowork/index.html')

@login_required
def perfil(request):
    return render(request, 'cowork/privada.html', {'titulo': 'Vista basada en función'})

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'cowork/privada.html'
    extra_context = {'titulo': 'Vista basada en clase'}

def error_404(request, exception):
    return render(request, '404.html')

def error_400(request, exception):
    return render(request, '400.html')


class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
