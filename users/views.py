from django.http.response import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer

# Create your views here.
class UsersList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_object(self, id):
    try:
      return User.objects.get(id=id)
    except User.DoesNotExist:
      raise Http404
  
  def get(self, request, id, format=None):
    user = self.get_object(id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

  def put(self, request, id, format=None):
    user = self.get_object(id)
    serializer = UserSerializer(user, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

