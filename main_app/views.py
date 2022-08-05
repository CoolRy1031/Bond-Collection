from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bond, Gadjet
from .forms import RatingForm



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
  rating_form = RatingForm()
  return render(request, 'bonds/detail.html', {'bond': bond, 'rating_form': rating_form})

def add_rating(request, bond_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit=False)
    new_rating.bond_id = bond_id
    new_rating.save()
  return redirect('bonds_detail', bond_id=bond_id)

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

class GadjetCreate(CreateView):
  model = Gadjet
  fields = '__all__'

class GadjetList(ListView):
  model = Gadjet

class GadjetDetail(DetailView):
  model = Gadjet

class GadjetUpdate(UpdateView):
  model = Gadjet
  fields = '__all__'

class GadjetDelete(DeleteView):
  model = Gadjet
  success_url = '/gadjets/'