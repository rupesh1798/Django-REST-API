from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from .serializers import PhotoSerializer, UserSerializer
from .models import Photos
from .permissions import IsOwner
from django.contrib.auth.models import User
from rest_framework.response import Response

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
