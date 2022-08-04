from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class BondCreate(CreateView):
  model = Bond
  fields = '__all__'
  success_url = '/bonds/'

class BondUpdate(UpdateView):
  model = Bond
  fields = '__all__'

class BondDelete(DeleteView):
  model = Bond
  success_url = '/bonds/'