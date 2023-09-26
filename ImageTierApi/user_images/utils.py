import os

from urllib.parse import urljoin
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import ImageSerializer, ExpireLinkSerializer
from .models import UserImage, ExpireLink
from user_accounts.models import UserAccount
from PIL import Image
from django.utils import timezone


def create_image(request):
    """
    POST - Post image
    """


    username = request.data.get('username')
    tier = request.data.get('tier')
    expire_link_duration = request.data.get('expire_link_duration')


    # Main urgent check of the data

    try:
        user = UserAccount.objects.get(username=username)
    except UserAccount.DoesNotExist:
        return Response({'Username': 'User with this username does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if tier not in [choice[0] for choice in settings.TIER_CHOICES]:
        return Response({'Tier': 'Such a tier does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    if user.tier != tier:
        return Response({'Tier': 'Tier does not match for the given username.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if tier == settings.TIER_CHOICES[2][0]:
        if expire_link_duration != None:
            expire_link_duration = int(expire_link_duration)
            if expire_link_duration < 30 or expire_link_duration > 30000:
                return Response({'Expire link duration': 'Make sure that this value is in the range of 30 to 30000'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Expire link error': 'Make sure that you sent expire_link_duration key.'}, status=status.HTTP_400_BAD_REQUEST)
    image_data = request.data.get('image')

    if not image_data:
        return Response({'error': 'No image data provided.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Main urgent check of the data

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
        
        account_tier = ''
        thumbnail_200_url = None
        thumbnail_400_url = None
        original_image_url = None

        if tier == settings.TIER_CHOICES[0][0]:
            account_tier = settings.TIER_CHOICES[0][1]
            thumbnail_200_size = 200
        elif tier == settings.TIER_CHOICES[1][0]:
            account_tier = settings.TIER_CHOICES[1][1]
            thumbnail_200_size = 200
        elif tier == settings.TIER_CHOICES[2][0]:
            account_tier = settings.TIER_CHOICES[2][1]
            thumbnail_200_size = 200

        if account_tier:
            image_serializer.instance.save()
            
            thumbnail_200 = image.copy()
            thumbnail_200.thumbnail((thumbnail_200_size, thumbnail_200_size))
            thumbnail_200_path = image_serializer.instance.image.path.replace(
                f".{image_serializer.instance.format}",
                f"@{user.username}_thumbnail_{thumbnail_200_size}px.{image_serializer.instance.format}"
            )
            thumbnail_200.save(thumbnail_200_path)
            thumbnail_200_url = urljoin(settings.MEDIA_URL, os.path.relpath(thumbnail_200_path, settings.MEDIA_ROOT))
            
            if tier == settings.TIER_CHOICES[1][0]:
                thumbnail_400 = image.copy()
                thumbnail_400.thumbnail((400, 400))
                thumbnail_400_path = image_serializer.instance.image.path.replace(
                    f".{image_serializer.instance.format}",
                    f"@{user.username}_thumbnail_400px.{image_serializer.instance.format}"
                )
                thumbnail_400.save(thumbnail_400_path)
                thumbnail_400_url = urljoin(settings.MEDIA_URL, os.path.relpath(thumbnail_400_path, settings.MEDIA_ROOT))
                
                original_image_url = urljoin(settings.MEDIA_URL, os.path.relpath(image_serializer.instance.image.path, settings.MEDIA_ROOT))
            elif tier == settings.TIER_CHOICES[2][0]:
                thumbnail_400 = image.copy()
                thumbnail_400.thumbnail((400, 400))
                thumbnail_400_path = image_serializer.instance.image.path.replace(
                    f".{image_serializer.instance.format}",
                    f"@{user.username}_thumbnail_400px.{image_serializer.instance.format}"
                )
                thumbnail_400.save(thumbnail_400_path)
                thumbnail_400_url = urljoin(settings.MEDIA_URL, os.path.relpath(thumbnail_400_path, settings.MEDIA_ROOT))
                
                original_image_url = urljoin(settings.MEDIA_URL, os.path.relpath(image_serializer.instance.image.path, settings.MEDIA_ROOT))
                print(request.data.get('expire_link_duration'))
                user_image_id = UserImage.objects.latest('created_at').id
                expire_link_data = {
                    'user_image': user_image_id,
                    'expire_link_duration': expire_link_duration,
                }
                expire_link_serializer = ExpireLinkSerializer(data=expire_link_data)
                if expire_link_serializer.is_valid():
                    expire_link_serializer.save()
                    user_image_expire_token = ExpireLink.objects.latest('created_at').expire_link
                    user_image_expire_link = reverse('expire-link-detail', args=[user_image_expire_token])
                    base_url = settings.BASE_URL
                    full_expire_url = f"{base_url}{user_image_expire_link}"

                    response_data = {"There is your thumbnail link that's 200px in height:": thumbnail_200_url}

                    if thumbnail_400_url:
                        response_data["There is your thumbnail link that's 400px in height:"] = thumbnail_400_url
                    if original_image_url:
                        response_data["There is your original uploaded image link: "] = original_image_url
                    if full_expire_url:
                        response_data["There is your expire link to your image with in seconds:"] = full_expire_url
                    return Response(response_data, status=status.HTTP_201_CREATED)
                return Response(expire_link_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            response_data = {"There is your thumbnail link that's 200px in height:": thumbnail_200_url}
            
            if thumbnail_400_url:
                response_data["There is your thumbnail link that's 400px in height:"] = thumbnail_400_url
            if original_image_url:
                response_data["There is your original uploaded image link: "] = original_image_url
            return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def receive_images(request):
    """
    GET - All images
    """

    images = UserImage.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


def receive_user_images(username):
    try:
        user = UserAccount.objects.get(username=username)
    except UserAccount.DoesNotExist:
        return Response({'error': 'User with this username does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    images = UserImage.objects.filter(user=user)
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)



def receive_expire_link(expire_link):
    try:
        expire_link_obj = ExpireLink.objects.get(expire_link=expire_link)
    except ExpireLink.DoesNotExist:
        return Response({'error': 'Expire link not found'}, status=status.HTTP_404_NOT_FOUND)
    image_path = expire_link_obj.user_image.image.path
    current_time = timezone.now()
    link_creation_time = expire_link_obj.created_at
    time_difference = current_time - link_creation_time
    if time_difference.total_seconds() > expire_link_obj.expire_link_duration:
        return Response({'error': 'Expire link has expired'}, status=status.HTTP_403_FORBIDDEN)
    with Image.open(image_path) as img:
        image_format = img.format.lower() if img.format else ''
    if image_format == 'jpeg':
        content_type = 'image/jpeg'
    elif image_format == 'png':
        content_type = 'image/png'
    else:
        content_type = 'image/jpg'
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    response = HttpResponse(image_data, content_type=content_type)
    return response