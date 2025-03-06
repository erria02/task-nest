from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import AutoParkModel, AutoParkSerializer, CarModel, CarSerializer
from rest_framework.response import Response

class CreateAutoParkApiView(CreateAPIView):
    serializer_class = AutoParkSerializer
    
class ListAutoParkApiView(ListAPIView):
    serializer_class=AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    
    
class CreateCarApiView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()


    def post(self,  *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        return Response(serializer.data, 201)
        
        
        