from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about' ),
  path('bonds/', views.bonds_index, name='bonds_index'),
  path('bonds/<int:bond_id>/', views.bonds_detail, name='bonds_detail'),
  path('bonds/create/', views.BondCreate.as_view(), name='bonds_create'),
  path('bonds/<int:pk>/update/', views.BondUpdate.as_view(), name='bonds_update'),
  path('bonds/<int:pk>/delete/', views.BondDelete.as_view(), name='bonds_delete'),

]