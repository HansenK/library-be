from django.contrib import admin

from books.models import Book, Tag

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'get_authors')

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Tag)