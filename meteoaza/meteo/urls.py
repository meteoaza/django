from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('docs/', views.docs, name='docs'),
    path('sin/', views.sin, name='sin'),
    path('about', views.about, name='about'),
]
