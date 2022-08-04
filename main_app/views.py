from django.shortcuts import render
from .models import Bond


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bonds_index(request):
  bonds = Bond.objects.all()
  return render(request, 'bonds/index.html', { 'bonds' : bonds})

def bonds_detail(request, bond_id):
  bond = Bond.objects.get(id=bond_id)
  return render(request, 'bonds/detail.html', {'bond': bond})