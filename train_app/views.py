from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegisterUserForm, LoginUserForm, IndexPageForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, AuthenticationForm
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
            form.save()
            return HttpResponseRedirect(reverse_lazy('main_name'))
        else:
            context = {
                'form': RegisterUserForm(request.POST),
            }
            return render(request, self.template_name, context = context)


# class LoginUser(LoginView):
#     template_name = 'train_app/login_user_form.html'
#     form_class = LoginUserForm
   
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = self.form_class 
#         return context
    
#     def get_success_url(self):
#         return reverse_lazy('main_name')


class LoginUser(TemplateView):
    template_name = 'train_app/login_user_form.html'
    form_class = LoginUserForm
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class 
        return context
    
    def get_success_url(self):
        return reverse_lazy('main_name')

    def post(self, request):
        form = LoginUserForm(request.POST)    
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('user_page_name'))

        return render(request, self.template_name, context={'form': form})

    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('main_name'))

class UserPage(TemplateView):
    template_name = 'train_app/user_page.html'
     
    def get(self, request):   
        if request.user.is_authenticated:
            return render(request, self.template_name, context={'user': request.user})
        else:
            return HttpResponseRedirect(reverse_lazy('login_user_name'))

class IndexPage(TemplateView):
    template_name = 'train_app/index.html'
    form = IndexPageForm

    def get(self, request):
        return render(request, self.template_name, context={'form':self.form})