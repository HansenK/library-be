from django.http.response import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from books.models import Book, Tag
from books.serializers import BookSerializer, TagSerializer

# Lists
class BooksList(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class TagsList(generics.ListAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

# Details
class BookDetail(generics.RetrieveUpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

  def get_object(self, id):
    try:
      return Book.objects.get(id=id)
    except Book.DoesNotExist:
      raise Http404
  
  def get(self, request, id):
    book = self.get_object(id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

  def put(self, request, id):
    book = self.get_object(id)
    serializer = BookSerializer(book, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)