from django.db import models

# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=50)
    weigth = models.IntegerField()
    code = models.CharField(max_length=50)
    url_image = models.ImageField(upload_to="medications/images")
    
    def __str__(self):
        return self.name