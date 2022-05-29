from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegisterUserForm, LoginUserForm, IndexPageForm, OrderTicketForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, AuthenticationForm
from .models import *
from django.db.models import Q
import json
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



class BuyTicket(TemplateView):
    template_name = 'train_app/buy_ticket.html'
    cupe = TypeTrainCars.objects.get(type_train_car = 'cupe')
    carriage = TypeTrainCars.objects.get(type_train_car = 'carriage')
    
    type_train_car_data = {
        'cupe': {
            'type_train_car': cupe.type_train_car,
            'number_of_seats': cupe.number_of_seats,
            'number_of_rows': cupe.number_of_rows,
            'place_size': cupe.place_size,
            'all_number_seats': cupe.all_number_seats,
        },
        'carriage': {
            'type_train_car': carriage.type_train_car,
            'number_of_seats': carriage.number_of_seats,
            'number_of_rows': carriage.number_of_rows,
            'place_size': carriage.place_size,
            'all_number_seats': cupe.all_number_seats,
        }
    }


    @staticmethod
    def train_composition(tr_num):
        train = Train.objects.get(number_train=f'{tr_num}')
        tr_comp = (train.train_composition.train_car_composition_json)
        return tr_comp

    def get(self,request):
        tr_num = request.GET.get('number_train')
        view_type_train_car = request.GET.get('type_train_car')
        first_view_type_train_car = TypeTrainCars.objects.get(type_train_car = f'{view_type_train_car}')

        return render(request, self.template_name, context={
            'tr_num':tr_num,
            'number_and_type_train_car':BuyTicket.train_composition(tr_num),
            'first_view_type_train_car':first_view_type_train_car,
            })
    
    
    @staticmethod
    def get_data_train_car(request):
        number_train = request.GET.get('number_train')
        type_train_car = request.GET.get('type_train_car')
        number_train_car = request.GET.get('number_train_car')

        data = {
            'type_train_car_data':BuyTicket.type_train_car_data[f'{type_train_car}'],
            'number_train':number_train,
            'type_train_car':type_train_car,
            'number_train_car':number_train_car,
        } 
        return JsonResponse(data)         

        
          


class IndexPage(TemplateView):
    template_name = 'train_app/index.html'
    form = IndexPageForm

    def get(self, request):
        return render(request, self.template_name, context={'form':self.form})

    def post(self, request):
        form = IndexPageForm(request.POST)
        
        if form.is_valid():
            from_city = form.cleaned_data.get('from_city')
            to_city = form.cleaned_data.get('to_city')
            all_train_paths = TrainPaths.objects.filter(Q(long_train_path__contains = from_city), Q(long_train_path__contains= to_city))
            if all_train_paths:
                valid_path = []           
                for path in all_train_paths:   
                    list_path:list = path.long_train_path.split('-')
                    if list_path.index(from_city) < list_path.index(to_city):
                        valid_path.append(path)

                city_stop_data = []
                for path_city in valid_path:    
                    city_from_to = []
                    city_from_to.append(path_city.city_set.get(city_name = from_city))
                    city_from_to.append(path_city.city_set.get(city_name = to_city))
                    city_stop_data.append(city_from_to)

                if city_stop_data:
                    numbers_valid_trains = []
                    train_composition = []
                    type_train_car = []
                    first_number_train_car = []
                    
                    for item in city_stop_data:
                        n_v_t = item[0].number_trains
                        numbers_valid_trains.append(n_v_t)
                        t_c = n_v_t.train_composition.train_car_composition_json
                        train_composition.append(t_c)
                        
                        if len(t_c) > 1:
                            t_t_c = []
                            f_n_t_c = []
                            for type_tc, first_number_tc in t_c.items():
                                t_t_c.append(type_tc)
                                f_n_t_c.append(first_number_tc[0])
                            type_train_car.append(t_t_c)
                            first_number_train_car.append(f_n_t_c)
                        else:
                            for type_tc, first_number_tc in t_c.items():
                                type_train_car.append(type_tc)
                                first_number_train_car.append(first_number_tc[0])
                            
                            
                                
                                


               


                
                clean = [from_city, to_city, all_train_paths, city_stop_data]
                
            else:
                return render(request, self.template_name, context={
                'form':form,
                'not_found': "Sorry, no tickets found",
            })


            return render(request, self.template_name, context={
                'form':form,
                'clean': clean,
                'city_ways_and_city_data': zip(valid_path, city_stop_data, numbers_valid_trains, first_number_train_car, type_train_car),
                'valid_path': valid_path[0].city_set.all(),
                'city_stop_data':city_stop_data,
                'numbers_valid_trains':numbers_valid_trains,
                'type_train_car': type_train_car,
                'first_number_train_car': first_number_train_car
            })
        return render(request, self.template_name, context={
                'form':form,
            })




class OrderTicketView(TemplateView):
    template_name = 'train_app/order_ticket.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return JsonResponse(json.loads(request.body))


            

