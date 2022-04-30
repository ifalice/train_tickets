from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegisterUserForm, LoginUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password, check_password

# Create your views here.

class Index(TemplateView):
    template_name = 'train_app/index.html'

    def get(self, request):
        return render(request, self.template_name)


class RegisterUser(TemplateView):
    template_name = 'train_app/register_user_form.html'
    form = RegisterUserForm()
    context = {
        'form': form,
    }

    def get(self, request):
        return render(request, self.template_name, context = self.context)

    def post(self, request):
        if RegisterUserForm(request.POST).is_valid():
            form = RegisterUserForm(request.POST)
            new_form = form.save(commit=False)
            new_form.password1 = make_password(new_form.password1, salt='pbkdf2_sha256')
            new_form.password2 = 0       
            new_form.save()
            return HttpResponseRedirect(reverse_lazy('main_name'))
        else:
            context = {
                'form': RegisterUserForm(request.POST),
            }
            return render(request, self.template_name, context = context)

class LoginUser(TemplateView):
    template_name = 'train_app/login_user_form.html'
    form = LoginUserForm()
    context = {
        'form': form
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse_lazy('user_page_name'))
        else:
            return render(request, self.template_name, context={'form': form})


class UserPage(TemplateView):
    template_name = 'train_app/user_page.html'
    
    def get(self, request):
        return render(request, self.template_name)