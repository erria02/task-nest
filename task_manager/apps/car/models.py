from django.db import models



    
class AutoParkModel(models.Model):
    class Meta:
        db_table = "auto_park"
    name = models.CharField(max_length=26)
    
    
class CarModel(models.Model):
    class Meta:
        db_table = "cars"
    
    name = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    age = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name="car")
    
