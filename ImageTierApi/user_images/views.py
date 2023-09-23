# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import create_image


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

@api_view(['POST'])
def post_images(request):
    if request.method == 'POST':
        return create_image(request)
