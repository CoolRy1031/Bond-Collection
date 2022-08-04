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