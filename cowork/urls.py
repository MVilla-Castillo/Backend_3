from django.urls import path

from . import views

app_name = 'cowork'

urlpatterns = [
    path('', views.index, name='index'),
]
