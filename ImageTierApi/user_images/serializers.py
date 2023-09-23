from rest_framework import serializers
from .models import UserImage

class ImageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserImage
        fields = '__all__'
