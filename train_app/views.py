from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegisterUserForm
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
           
            RegisterUserForm(request.POST).save()
            return HttpResponseRedirect(reverse_lazy('main_name'))
        else:
            context = {
                'form': RegisterUserForm(request.POST),
            }
            return render(request, self.template_name, context = context)
            