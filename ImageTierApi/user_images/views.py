from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import create_image, receive_images, receive_user_images, receive_expire_link
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


@api_view(['GET'])
def get_user_images(request, username):
    if request.method == 'GET':
        return receive_user_images(username)

@api_view(['POST'])
def post_image(request):
    if request.method == 'POST':
        return create_image(request)


@api_view(['GET'])
def get_expire_link(request, expire_link_token):
    if request.method == 'GET':
        return receive_expire_link(expire_link_token)