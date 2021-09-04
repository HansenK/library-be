from django.db import models

# Create your models here.
class Author(models.Model):
  def __str__(self):
    return self.first_name + self.last_name

  first_name = models.CharField(max_length=128)
  last_name = models.CharField(max_length=128, blank=True)

  class Meta:
    ordering = ['first_name']