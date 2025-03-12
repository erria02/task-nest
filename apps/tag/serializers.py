from rest_framework.serializers import ModelSerializer
from .models import TagModel

class TagSerializer(ModelSerializer):
    class Meta:
        model = TagModel
        fields = '__all__'