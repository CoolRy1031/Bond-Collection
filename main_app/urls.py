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
  path('bonds/<int:bond_id>/add_rating/', views.add_rating, name="add_rating"),
  path('gadjets/create/', views.GadjetCreate.as_view(), name='gadjets_create'),
  path('gadjets/<int:pk>/', views.GadjetDetail.as_view(), name='gadjets_detail'),
  path('gadjets/', views.GadjetList.as_view(), name='gadjets_index'),
  path('gadjets/<int:pk>/update/', views.GadjetUpdate.as_view(), name='gadjets_update'),
  path('toys/<int:pk>/delete/', views.GadjetDelete.as_view(), name='gadjets_delete'),

]