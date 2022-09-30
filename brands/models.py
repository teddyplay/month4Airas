from django.db import models
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=500, verbose_name="Название Автомобиля", null=True)
    image = models.ImageField(upload_to=" ",null=True)
    # name = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="+", null=True)
    # engine = models.CharField(max_length=100, verbose_name="Двигатель", null=True)
    # hp = models.IntegerField(max_length=1000, verbose_name="Лошадиные силы", null=True)
    # nm = models.IntegerField(max_length=1000, verbose_name="Ньютон метр", null=True)
    # series = models.TextField(max_length=500, null=True)


    def __str__(self):
        return str(self.name)





