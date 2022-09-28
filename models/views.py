from django.shortcuts import render, get_object_or_404
from . import models

def all_models(request, id):
    show = get_object_or_404(models.Model, id=id)
    return render(request, "all_models.html", {"show":show})




