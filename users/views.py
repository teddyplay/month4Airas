from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, LoginForm
# def register(request):

#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Создан аккаунт {username}')
#             return HttpResponse("регистариция прошла успешно!")
#         else:
#             form = UserRegisterForm()
#             return render(request, "register.html", {"form":form})
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import UserRegisterForm




# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Создан аккаунт {username} )))')
#             return redirect(reversed('blog-home'))
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})







# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
#             return redirect(reverse('all_brands'))
#     else:
#         form = UserRegisterForm()
#     return render(request, 'all_brands.html', {'form': form})
#
#
# class Login(LoginView):
#     form_class = LoginView
#     template_name = "login.html"
#     success_url = "/all_brands/"
#
#     def get_success_url(self):
#         return self.success_url
#


# # @login_required
# def profile(request):
#     return render(request, 'profile.html')





class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = "/login/"


class NewLoginView(LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"
    success_url = "/all_brands/"

    def get_success_url(self):
        return self.success_url


# class UserListView(generic.ListView):
#     template_name = "users.html"
#     queryset = User.objects.all()
#
#     def get_queryset(self):
#         return self.queryset