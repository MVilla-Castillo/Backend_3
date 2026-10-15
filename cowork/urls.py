from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'cowork'

router = DefaultRouter()
router.register('sedes', views.SedeViewSet)
router.register('salas', views.SalaViewSet)
router.register('clientes', views.ClienteViewSet)
router.register('reservas', views.ReservaViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('api/', include(router.urls)),
]
