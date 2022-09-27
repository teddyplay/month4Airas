from django.db import models

from django.db import models

from brands.models import Brand


class Model(models.Model):
    name = models.ForeignKey(Brand,on_delete=models.CASCADE, null=True)
    engine = models.TextField(max_length=100, verbose_name="Двигатель", null=True)
    hp = models.IntegerField(max_length=1000, verbose_name="Лошадиные силы", null=True)
    nm = models.IntegerField(max_length=1000, verbose_name="Ньютон метр", null=True)
    # image = models.ImageField(upload_to="", null=True)
    # series = models.TextField(max_length=500, null=True)


    def __str__(self):
        return str(self.name)
