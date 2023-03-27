from urllib.parse import urlencode

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import FishFactory
from .models import Fish


class TestGetFishView(APITestCase):
    url = reverse('creatures:fish')

    @classmethod
    def setUpTestData(cls):
        cls.fish = FishFactory.create()

    def test_get_fish(self):
        params = {'type': self.fish.type}
        encoded_params = urlencode(params)

        url = self.url + '?{}'.format(encoded_params)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        queryset = Fish.objects.filter(type__icontains=self.fish.type)
        self.assertEqual(len(response.data), queryset.count())
