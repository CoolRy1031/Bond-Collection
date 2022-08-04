from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about' ),
  path('bonds/', views.bonds_index, name='bonds_index'),
  path('bonds/<int:bond_id>/', views.bonds_detail, name='bonds_detail'),

]