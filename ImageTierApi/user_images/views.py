from rest_framework import generics
from .models import UserImage
from .serializers import ImageSerializer

class ImageCreateView(generics.CreateAPIView):
    queryset = UserImage.objects.all()
    serializer_class = ImageSerializer
