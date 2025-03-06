from rest_framework.serializers import ModelSerializer
from .models import CarModel, AutoParkModel

class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        read_only_fields=(
            'auto_park',
        )

    
   
class AutoParkSerializer(ModelSerializer):
    car = CarSerializer(read_only=True, many=True)
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'car')

    


