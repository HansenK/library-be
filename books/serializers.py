from django.db.models import fields
from rest_framework import serializers

from books.models import Book, Tag
from authors.serializers import AuthorSerializer

class TagSerializer(serializers.HyperlinkedModelSerializer):
  slug = fields.SlugField()

  class Meta:
    model = Tag
    fields = [
      'id',
      'label',
      'slug'
    ]
    read_only_fields = (
      'id',
    )

class BookSerializer(serializers.HyperlinkedModelSerializer):
  authors = AuthorSerializer(many=True)
  tags = TagSerializer(many=True)

  class Meta:
    model = Book
    fields = [
      'id',
      'title',
      'authors',
      'description',
      'tags'
    ]
    read_only_fields = (
      'id',
    )