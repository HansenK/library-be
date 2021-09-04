from rest_framework import serializers

from users.models import User
from books.serializers import BookSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
  read_books = BookSerializer(many=True)
  wish_list = BookSerializer(many=True)

  class Meta:
    model = User
    fields = [
      "id",
      "first_name",
      "last_name",
      "email",
      "role",
      "read_books",
      "wish_list"
    ]
    read_only_fields = (
        "id",
        "email",
    )