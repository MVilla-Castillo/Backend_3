from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cowork.urls')),
]

handler404 = 'cowork.views.error_404'
handler400 = 'cowork.views.error_400'
