from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = [
      "id",
      "first_name",
      "last_name",
      "email"
    ]
    read_only_fields = (
        "id",
        "email",
    )