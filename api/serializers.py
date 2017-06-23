from rest_framework import serializers
from .models import Photos
from django.contrib.auth.models import User


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Photos
        fields = ('name', 'owner', 'image', 'created')
        read_only_fields = ('created',)

class UserSerializer(serializers.ModelSerializer):
    photos = serializers.PrimaryKeyRelatedField(many=True, queryset=Photos.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'photos')
