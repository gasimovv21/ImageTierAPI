import os

from urllib.parse import urljoin
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import ImageSerializer
from .models import UserImage
from user_accounts.models import UserAccount
from PIL import Image


def create_image(request):
    """
    POST - Post image
    """


    username = request.data.get('username')
    tier = request.data.get('tier')

    try:
        user = UserAccount.objects.get(username=username)
    except UserAccount.DoesNotExist:
        return Response({'error': 'User with this username does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if tier not in [choice[0] for choice in settings.TIER_CHOICES]:
        return Response({'error': 'Such a tier does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    if user.tier != tier:
        return Response({'error': 'Tier does not match for the given username.'}, status=status.HTTP_400_BAD_REQUEST)
    
    image_data = request.data.get('image')

    if not image_data:
        return Response({'error': 'No image data provided.'}, status=status.HTTP_400_BAD_REQUEST)

    user_data = {
        'user': user.id,
        'image': image_data,
    }

    image_serializer = ImageSerializer(data=user_data)
    
    if image_serializer.is_valid():
        image_serializer.save()
        image = Image.open(image_serializer.instance.image.path)
        image_serializer.instance.format = image.format.lower() if image.format else ''
        image_serializer.instance.width, image_serializer.instance.height = image.size
        
        tier_message = ''
        thumbnail_200_url = None
        thumbnail_400_url = None
        original_image_url = None

        if tier == settings.TIER_CHOICES[0][0]:
            tier_message = settings.TIER_CHOICES[0][1]
            thumbnail_200_size = 200
        elif tier == settings.TIER_CHOICES[1][0]:
            tier_message = settings.TIER_CHOICES[1][1]
            thumbnail_200_size = 200
        elif tier == settings.TIER_CHOICES[2][0]:
            tier_message = settings.TIER_CHOICES[2][1]
            thumbnail_200_size = 200

        if tier_message:
            image_serializer.instance.save()
            
            thumbnail_200 = image.copy()
            thumbnail_200.thumbnail((thumbnail_200_size, thumbnail_200_size))
            thumbnail_200_path = image_serializer.instance.image.path.replace(
                f".{image_serializer.instance.format}",
                f"@{user.username}_thumbnail_{thumbnail_200_size}px.{image_serializer.instance.format}"
            )
            thumbnail_200.save(thumbnail_200_path)
            thumbnail_200_url = urljoin(settings.MEDIA_URL, os.path.relpath(thumbnail_200_path, settings.MEDIA_ROOT))
            
            if tier in [settings.TIER_CHOICES[1][0], settings.TIER_CHOICES[2][0]]:
                thumbnail_400 = image.copy()
                thumbnail_400.thumbnail((400, 400))
                thumbnail_400_path = image_serializer.instance.image.path.replace(
                    f".{image_serializer.instance.format}",
                    f"@{user.username}_thumbnail_400px.{image_serializer.instance.format}"
                )
                thumbnail_400.save(thumbnail_400_path)
                thumbnail_400_url = urljoin(settings.MEDIA_URL, os.path.relpath(thumbnail_400_path, settings.MEDIA_ROOT))
                
                original_image_url = urljoin(settings.MEDIA_URL, os.path.relpath(image_serializer.instance.image.path, settings.MEDIA_ROOT))

            response_data = {"message": f"{tier_message}!", "thumbnail_url_200px": thumbnail_200_url}
            
            if thumbnail_400_url:
                response_data["thumbnail_url_400px"] = thumbnail_400_url
            if original_image_url:
                response_data["original_image_url"] = original_image_url
            return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)







def receive_images(request):
    """
    GET - All images
    """

    images = UserImage.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


def receive_user_image(request, username):
    try:
        user = UserAccount.objects.get(username=username)
    except UserAccount.DoesNotExist:
        return Response({'error': 'User with this username does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    images = UserImage.objects.filter(user=user)
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


