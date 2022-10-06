from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import RegistrationForm, LoginForm, MyPasswordChangeForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy


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


# class NewLoginView(LoginView):
#     form_class = LoginForm
#     template_name = "registration/account.html"
#     success_url = "/all_brands/"

    # def get_success_url(self):
    #     return self.success_url

def profile(request):
    return render(request, 'profile.html')
#


# class MyPasswordChangeView(generic.CreateView):
#     form_class = MyPasswordChangeForm
#     template_name = 'registration/account.html'
#     success_url = '/all_brands/'

#
#     def get_success_url(self):
#         return self.success_url

# def change(request):
#     global form
#     u = User.objects.get(username=request.user)
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             old_password = request.POST.get("old_password")
#             new_pass = request.POST.get("new_password")
#             new_pass_rep = request.POST.get("new_password_repeat")
#             if check_password(old_password,u.password):
#                 return HttpResponse('ok')
#             else:
#                 return HttpResponse('bad')
#     return render(request, 'profile.html',{"form":change})
# class UserListView(generic.ListView):
#     template_name = "users.html"
#     queryset = User.objects.all()
#
#     def get_queryset(self):
#         return self.queryset

# def password_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
# #             update_session_auth_hash(request, form.user)
# def change(request, id):
#     user = get_object_or_404(User, id=id)
#     if request.method == "POST":
#         # getting form input values from your HTML Form.
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         user.set_password(password1)
#         user.set_password(password2)
#         user.save()
#         return redirect(reverse("change"))
#     return render(request, 'registration/account.html', {"form":user})
class MyPasswordChangeView(PasswordChangeView):
    template_name = "registration/account.html"
    success_url = reverse_lazy("users:change")


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/account_change.html"



