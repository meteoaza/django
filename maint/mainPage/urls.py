from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sens/', views.sens, name='sens'),
    path('report/', views.report, name='report'),
    path('log/', views.log, name='log'),
    path('clear_log/', views.clear_log, name='clear'),
    path('clear_rep/', views.clear_rep, name='clear'),
]
