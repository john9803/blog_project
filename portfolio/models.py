from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length = 255) #charfield 는 문자열을 받아주는 기능을 수행하게 된다.
    image = models.ImageField(upload_to='image/')# imagefield 는 이미지를 받아주는 기능을 수행하게 된다.
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title