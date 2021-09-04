from authors.serializers import AuthorSerializer
from rest_framework import generics

from authors.models import Author

# Create your views here.
class AuthorsList(generics.ListAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer