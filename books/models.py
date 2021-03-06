from django.contrib import admin
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from authors.models import Author

# Create your models here.
class Tag(models.Model):
  def __str__(self):
    return self.label

  label = models.CharField(max_length=128)
  slug = models.SlugField(null=True, blank=True, editable=False)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.label)

    return super().save(*args, **kwargs)

  
class Book(models.Model):
  def __str__(self):
    return self.title

  title = models.CharField(max_length=128)
  authors = models.ManyToManyField(Author, related_name="books")
  description = models.TextField(blank=True)
  tags = models.ManyToManyField(Tag, related_name="tags")

  @admin.display(description='Authors')
  def get_authors(self):
    return ", ".join([author.first_name + " " + author.last_name for author in self.authors.all()])

  class Meta:
    ordering = ['title']