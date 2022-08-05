from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RATINGS = (
  ('B', 'Bad'),
  ('O', 'OK'),
  ('G', 'Great')
)

# Create your models here.
class Gadjet(models.Model):
  name = models.CharField(max_length=50)

  def __str__ (self):
    return self.name
  
  def get_absolute_url(self):
      return reverse('gadjets_detail', kwargs={"pk": self.id})
  

class Bond(models.Model):
  movie = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  gadjets = models.ManyToManyField(Gadjet)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.movie

  def get_absolute_url(self):
    return reverse('bonds_detail', kwargs={'bond_id': self.id})

class Rating(models.Model):
  type = models.CharField(
    max_length=1,
    choices=RATINGS,
    default=RATINGS[2][0]
  )
  bond = models.ForeignKey(Bond, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_type_display()}"
