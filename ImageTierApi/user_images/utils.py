from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer
from .models import UserImage
from user_accounts.models import UserAccount
from PIL import Image

def create_image(request):
    username = request.data.get('username')
    tier = request.data.get('tier')

    try:
        user = UserAccount.objects.get(username=username)
    except UserAccount.DoesNotExist:
        return Response({'error': 'User with this username does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if tier not in ('Basic', 'Premium', 'Enterprise'):
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
        image_serializer.instance.save()

        return Response(image_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def receive_images(request):
    images = UserImage.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)
