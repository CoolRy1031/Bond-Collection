from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bond, Gadjet
from .forms import RatingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def bonds_index(request):
  bonds = Bond.objects.filter(user=request.user)
  return render(request, 'bonds/index.html', { 'bonds' : bonds})

@login_required
def bonds_detail(request, bond_id):
  bond = Bond.objects.get(id=bond_id)
  gadjets_bond_doesnt_have = Bond.objects.exclude(id__in = bond.gadjets.all().values_list('id'))
  rating_form = RatingForm()
  return render(request, 'bonds/detail.html', {'bond': bond, 'rating_form': rating_form, 'gadjets': gadjets_bond_doesnt_have})

@login_required
def add_rating(request, bond_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit=False)
    new_rating.bond_id = bond_id
    new_rating.save()
  return redirect('bonds_detail', bond_id=bond_id)

class BondCreate(LoginRequiredMixin
,CreateView):
  model = Bond
  fields = ['movie', 'description', 'year']
  success_url = '/bonds/'

  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BondUpdate(LoginRequiredMixin
,UpdateView):
  model = Bond
  fields = '__all__'

class BondDelete(LoginRequiredMixin
,DeleteView):
  model = Bond
  success_url = '/bonds/'

class GadjetCreate(LoginRequiredMixin
,CreateView):
  model = Gadjet
  fields = '__all__'

class GadjetList(LoginRequiredMixin
,ListView):
  model = Gadjet

class GadjetDetail(LoginRequiredMixin
,DetailView):
  model = Gadjet
  fields='__all__'

class GadjetUpdate(UpdateView):
  model = Gadjet
  fields = '__all__'

class GadjetDelete(LoginRequiredMixin
,DeleteView):
  model = Gadjet
  success_url = '/gadjets/'

@login_required
def assoc_gadjet(request, bond_id, gadjet_id):
  Bond.objects.get(id=bond_id).gadjets.add(gadjet_id)
  return redirect('bonds_detail', bond_id=bond_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('bonds_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
