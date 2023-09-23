# utils.py
import requests

from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer
from user_accounts.models import UserAccount

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

    user_data = {
        'user': user.id,
        'image': request.data.get('image'),
    }
    serializer = ImageSerializer(data=user_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
