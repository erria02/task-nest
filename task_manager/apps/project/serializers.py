from .models import ProjectModel
from rest_framework.serializers import ModelSerializer

class ProjectSerializers(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ('id', 'title')
