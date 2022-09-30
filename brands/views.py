# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
# from .forms import PostForm
from django.shortcuts import redirect
from models.models import Model


def all_brands(request):
    cars = models.Brand.objects.all()
    return render(request, "all_brands.html", {"car":cars})



# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.POST
#             post.save()
#             return redirect('post_detail')
#     else:
#         form = PostForm()
#     return render(request, 'add_models.html', {'form': form})
# def post_edit(request, pk):
#     post = get_object_or_404(Model, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('post_detail')
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'add_models.html', {'form': form})
