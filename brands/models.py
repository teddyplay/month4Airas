from django.db import models

# from models.models import Model


class Brand(models.Model):
    name = models.CharField(max_length=500, verbose_name="Название Автомобиля", null=True)
    image = models.ImageField(upload_to=" ",null=True)



    def __str__(self):
        return str(self.name)



