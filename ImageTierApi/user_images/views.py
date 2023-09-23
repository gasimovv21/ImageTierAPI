from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import create_image, receive_images

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/upload/',
            'method': 'POST',
            'body': None,
            'description':  [
                'Uploading new image => POST',
            ]
        },
    ]
    return Response(routes)

@api_view(['GET'])
def get_images(request):
    if request.method == 'GET':
        return receive_images(request)

@api_view(['POST'])
def post_image(request):
    if request.method == 'POST':
        return create_image(request)
