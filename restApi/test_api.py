from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from restApi import views 
from restApi.models import RestApi
from restApi.serializers import RestApiSerializer

class TodoListTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo = RestApi.objects.create(id=1,name="test")
        self.todoSerialized = RestApiSerializer(self.todo).data

    def test_can_get_api(self):
        url = reverse(views.todo_detail)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_api(self):
        url = reverse(views.todo_detail)
        data = self.todoSerialized
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_update_api(self):
        url = reverse(views.todo_detail)
        data = {"id":1,"name": "Test Todo Update"}
        response = self.client.put(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_api(self):
        #Le pasamos directamente la url con el id a eliminar, en este caso el 1 que creamos en el setUp
        response = self.client.delete('/api/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    

