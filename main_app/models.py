from django.db import models
from django.urls import reverse

# Create your models here.
class Bond(models.Model):
  movie = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()

  def __str__(self):
    return self.movie

  def get_absolute_url(self):
    return reverse('bonds_detail', kwargs={'bond_id': self.id})