from rest_framework.serializers import ModelSerializer
from .models import TagModel

class TagSerializer(ModelSerializer):
    class Meta:
        model = TagModel
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = ('name',)
>>>>>>> project
