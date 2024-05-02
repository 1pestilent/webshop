from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from products.models import Basket, Order, OrderDetails
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form,
               'title': 'Вход в личный кабинет'}
    return render(request, 'users/login.html',context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, 'Регистрация прошла успешно!')
           return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form,
               'title': 'Регистрация пользователя'
               }
    return render(request, 'users/reg.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    orders = Order.objects.filter(user=request.user)

    order_details = {}
    for order in orders:
        order_details[order] = OrderDetails.objects.filter(order=order)

    context = {'title': 'Bosfor - профиль',
                'form': form,
                'baskets': Basket.objects.filter(user=request.user),
                'orders': orders,
            }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))