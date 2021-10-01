from django.contrib import admin

from users.models import User, ReadBook

# custom admin models
class ReadBookAdmin(admin.ModelAdmin):
  list_display = ('user', 'book', 'end_date')

class UserAdmin(admin.ModelAdmin):
  def name(self):
    return self.first_name + " " + self.last_name

  list_display = (name, 'email')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ReadBook, ReadBookAdmin)