from rest_framework import serializers
from .models import UserImage, ExpireLink
from django.core.validators import MinValueValidator, MaxValueValidator


class ImageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    expire_link_duration = serializers.IntegerField(required=False)

    class Meta:
        model = UserImage
        fields = '__all__'


class ExpireLinkSerializer(serializers.ModelSerializer):
    expire_link_duration = serializers.IntegerField(
        validators=[
            MinValueValidator(30),
            MaxValueValidator(30000),
        ]
    )

    class Meta:
        model = ExpireLink
        fields = '__all__'