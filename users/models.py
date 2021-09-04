from django.db import models

# Create your models here.
class User(models.Model):

  def __str__(self):
        return self.email

  email = models.EmailField(unique=True, max_length=100)
  first_name = models.CharField(max_length=128)
  last_name = models.CharField(max_length=128, blank=True)