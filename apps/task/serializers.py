from rest_framework.serializers import ModelSerializer
from .models import TaskModel
from apps.tag.serializers import TagSerializer
from apps.tag.models import TagModel

class TaskSerializer(ModelSerializer):
    tag = TagSerializer(many=True)
    class Meta:
        model = TaskModel
        fields = ('name', 'description', 'deadline', 'tag')
    

  
    def create(self, validated_data:dict):
        validated_data.setdefault('tag', None)
        tag = validated_data.pop('tag')
        if tag:
            list_tag = []
            for i in tag:
                tag = TagModel.objects.create(**i)
                tag.save()
                list_tag.append(tag.id)
            task = TaskModel.objects.create(**validated_data)
            task.tag.add(*list_tag)
            task.save()
            return task
        task = TaskModel.objects.create(**validated_data)
        task.save()
        return task
        
