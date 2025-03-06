from .models import TaskModel, TagModel
from rest_framework.serializers import ModelSerializer
from django.db.transaction import atomic
class TagSerializer(ModelSerializer):
    class Meta:
        model = TagModel
        fields = ('id', 'title')
        
class TaskSerializer(ModelSerializer):
    tag = TagSerializer()
    class Meta:
        model = TaskModel
        fields = ('id', 'title', 'priority', 'completed', 'description', 'created_at', 'updated_at', 'tag')
        
    @atomic
    def create(self, validated_data):
        tag = validated_data.pop('tag')
        tag = TagModel.objects.create(**tag)
        task = TaskModel.objects.create(**validated_data, tag = tag)
        task.save()
        return task
    
class UpdateTaskSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ('id', 'title', 'priority', 'completed', 'description', 'created_at', 'updated_at', 'tag')

   