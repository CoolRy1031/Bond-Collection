from django.db import models
from django.urls import reverse

RATINGS = (
  ('B', 'Bad'),
  ('O', 'OK'),
  ('G', 'Great')
)

# Create your models here.
class Bond(models.Model):
  movie = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()

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
