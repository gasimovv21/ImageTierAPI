from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import UserImage, ExpireLink
from user_accounts.models import UserAccount
from django.core.files.uploadedfile import SimpleUploadedFile


with open('media/images/ELTUN_GASIMOV.png', 'rb') as image_file:
    image = SimpleUploadedFile("ELTUN_GASIMOV.png", image_file.read(), content_type="image/png")


class ImageAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = "testuser"
        self.tier = "Basic"

        self.image_data = {
            "username": self.username,
            "tier": self.tier,
            "image": image,
        }
        self.user = UserAccount.objects.create(username=self.username, tier=self.tier)

    def test_create_image(self):
        url = reverse("image-upload")
        response = self.client.post(url, data=self.image_data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserImage.objects.count(), 1)
        user_image = UserImage.objects.get()
        self.assertEqual(user_image.user, self.user)

    def test_get_images(self):
        url = reverse("images")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_images(self):
        url = reverse("user-images", args=[self.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_expire_link(self):
        user_image = UserImage.objects.create(user=self.user, image=image)
        expire_link = ExpireLink.objects.create(user_image=user_image, expire_link_duration=60)
        url = reverse("expire-link-detail", args=[expire_link.expire_link_token])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
