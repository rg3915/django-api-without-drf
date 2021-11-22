import json

from django.test import TestCase

from .models import Video


class VideoTest(TestCase):

    def setUp(self):
        self.payload = {
            "title": "Dica #47 - DRF: djoser - Django REST framework",
            "link": "https://youtu.be/HUtG2Eg47Gw",
            "view": 307
        }

    def test_video_create(self):
        response = self.client.post(
            '/api/v2/videos/',
            data=self.payload,
            content_type='application/json'
        )
        resultado = json.loads(response.content)
        esperado = {
            "data": {
                "id": 1,
                **self.payload
            }
        }
        self.assertEqual(esperado, resultado)

    def test_video_list(self):
        Video.objects.create(**self.payload)

        response = self.client.get(
            '/api/v2/videos/',
            content_type='application/json'
        )
        resultado = json.loads(response.content)
        esperado = {
            "data": [
                {
                    "id": 1,
                    **self.payload
                }
            ]
        }
        self.assertEqual(esperado, resultado)

    def test_video_detail(self):
        Video.objects.create(**self.payload)

        response = self.client.get(
            '/api/v2/videos/1/',
            content_type='application/json'
        )
        resultado = json.loads(response.content)
        esperado = {
            "data": {
                "id": 1,
                **self.payload
            }
        }
        self.assertEqual(esperado, resultado)

    def test_video_update(self):
        Video.objects.create(**self.payload)

        data = {
            "title": "Dica #47 - DRF: djoser"
        }

        response = self.client.post(
            '/api/v2/videos/1/',
            data=data,
            content_type='application/json'
        )
        resultado = json.loads(response.content)
        esperado = {
            "data":
            {
                "id": 1,
                "title": "Dica #47 - DRF: djoser",
                "link": "https://youtu.be/HUtG2Eg47Gw",
                "view": 307
            }
        }
        self.assertEqual(esperado, resultado)

    def test_video_delete(self):
        Video.objects.create(**self.payload)

        response = self.client.delete(
            '/api/v2/videos/1/',
            content_type='application/json'
        )
        resultado = json.loads(response.content)
        esperado = {"data": "Item deletado com sucesso."}

        self.assertEqual(esperado, resultado)
