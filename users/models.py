from django.db import models

from books.models import Book

USER_ROLES = (
  ('admin', 'Admin'),
  ('reader', 'Reader'),
  ('book_manager', "Book Manager")
)

# Create your models here.
class User(models.Model):
  def __str__(self):
    return self.email

  email = models.EmailField(unique=True, max_length=100)
  first_name = models.CharField(max_length=128)
  last_name = models.CharField(max_length=128, blank=True)
  role = models.CharField(max_length=128, choices=USER_ROLES, default='reader')
  wish_list = models.ManyToManyField(Book, related_name="wish_list", blank=True)

  class Meta:
    ordering = ['email']

class ReadBook(models.Model):
  def __str__(self):
    return str(self.end_date)

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="read_books")
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  end_date = models.DateField()

  class Meta:
    ordering = ['end_date']