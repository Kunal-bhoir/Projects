from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='basic-home'),
    path('report/',views.report, name='basic-report'),
]