from django.shortcuts import render, get_object_or_404
from . import models


def all_brands(request):
    car = models.Brand.objects.all()
    return render(request, "all_brands.html",{"car":car})




# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.POST
#             post.save()
#             return redirect("add_models", pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'post_edit', {"form": form})
# def post_new(request):
#     if request.method == "POST":
#         form = AddModel(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return render(request, "add_comment.html")
#     else:
#         form = AddModel()
#     return render(request, "all_models.html", {'form': form})

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
#     return render(request, 'add_comment.html', {'form': form})


# def add_model(request):
#     if request.method == "GET":
#         return render(request, "add_comment.html", context={"post_form":AddModel})
#     if request.method == "POST":
#         print(request.POST)
#         if form.is_valid():
#             AddModel.objects.create(
#                 name = form.cleaned_data.get('name'),
#                 engine = form.cleaned_data.get('engine'),
#                 hp = form.cleaned_data.get('hp'),
#                 nm = form.cleaned_data.get('nm'),
#                 image = form.cleaned_data.get('image'),
#                 series = form.cleaned_data.get('series'),
#             )
#             return redirect('/')
#         else:
#             return HttpResponse("Error")


# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             # post.published_date = timezone.now()
#             post.save()
#             return redirect(reverse("test"))
#     else:
#         form = PostForm()
#     return render(request, 'add_comment.html', {'form': form})

# def add_models(request):
#     method = request.method
#     if method == "POST":
#         form = forms.PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Форма успешна создана!")
#     else:
#         form = forms.PostForm()
#
#     return render(request,"add_comment.html", {"form":form})
# def add_brands(request):
#     form = PostForm(request.POST, request.FILES)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return HttpResponse('рвамым')
#     return render(request, 'add_comment.html', {'form': form})

