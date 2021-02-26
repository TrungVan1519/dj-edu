from django.urls import path

from . import views

app_name = 'pollers'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/vote/', views.vote, name='vote'),
]
