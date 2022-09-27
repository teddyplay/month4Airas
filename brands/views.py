from django.shortcuts import render
from . import models


def all_brands(request):
    cars = models.Brand.objects.all()
    return render(request, "all_brands.html", {"car":cars})