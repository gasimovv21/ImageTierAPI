from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserImage
from .serializers import ImageSerializer
from user_accounts.models import UserAccount

class ImageCreateView(generics.CreateAPIView):
    queryset = UserImage.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        tier = request.data.get('tier')
        print(tier)

        try:
            user = UserAccount.objects.get(username=username)
        except UserAccount.DoesNotExist:
            return Response({'error': 'User with this username does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if tier not in ('Basic', 'Premium', 'Enterprise'):
            return Response({'error': 'Such a tier does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        if user.tier != tier:
            return Response({'error': 'Tier does not match for the given username.'}, status=status.HTTP_400_BAD_REQUEST)


        return super().create(request, *args, **kwargs)


