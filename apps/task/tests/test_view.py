from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from ..models import TaskModel
from apps.tag.models import TagModel
from rest_framework import status

class TaskTestCase(APITestCase):
    def _createtask(self):
        sample_task = {
            'name': 'test',
            'description': 'test'
        }
        
        self.client.post(reverse('tasks_create'), sample_task)
    
    def test_create_task(self):
        count = TaskModel.objects.count()
        
        tag = TagModel.objects.create(name='test')
        sample_task = {
            "name": "test",
            "description":"test",
        }
        
        response = self.client.post(reverse('tasks_create'), sample_task)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TaskModel.objects.count(), count+1)
        
    def test_list_task(self):
        self._createtask()
        self.client.get(reverse('tasks_list'))
        
    