from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=500, verbose_name="Название Автомобиля", null=True)
    # image = models.ForeignKey(, on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.name

