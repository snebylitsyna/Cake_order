import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group

from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models
from . import forms


class GoodListView(ListView):
    model = models.Good
    template_name = 'cakes.html'
    context_object_name = 'cakes'


class GoodCreateView(CreateView):
    model = models.Good
    form_class = forms.GoodForm
    template_name = 'good_create.html'
    success_url = reverse_lazy('good_list')


class GoodUpdateView(UpdateView):
    model = models.Good
    form_class = forms.GoodForm
    template_name = 'good_update.html'
    success_url = reverse_lazy('good_list')


class GoodDeleteView(DeleteView):
    model = models.Good
    success_url = reverse_lazy('good_list')
    template_name = 'good_delete.html'


def conf_del_good(request, pk):
    good = get_object_or_404(models.Good, pk=pk)
    return render(request, 'conf_del_good.html', {'good': good})


class ManufacturerListView(ListView):
    model = models.Manufacturer
    template_name = 'manufacturers.html'
    context_object_name = 'manufacturers'


class ManufacturerCreateView(CreateView):
    model = models.Manufacturer
    form_class = forms.ManufacturerForm
    template_name = 'manufacturer_create.html'
    success_url = reverse_lazy('manufacturer_list')


def admin_edit(request):
    return render(request, 'admin_edit.html')


def main(request):
    return render(request, 'main.html')


class CityListView(ListView):
    model = models.City
    template_name = 'cities.html'
    context_object_name = 'cities'


class CityCreateView(CreateView):
    model = models.City
    form_class = forms.CityForm
    template_name = 'city_create.html'
    success_url = reverse_lazy('city_list')


class ShopListView(ListView):
    model = models.Shop
    template_name = 'shops.html'
    context_object_name = 'shops'


class ShopCreateView(CreateView):
    model = models.Shop
    form_class = forms.ShopForm
    template_name = 'shop_create.html'
    success_url = reverse_lazy('shop_list')


class ShopUpdateView(UpdateView):
    model = models.Shop
    form_class = forms.ShopForm
    template_name = 'shop_update.html'
    success_url = reverse_lazy('shop_list')


class ShopDeleteView(DeleteView):
    model = models.Shop
    success_url = reverse_lazy('shop_list')
    template_name = 'shop_delete.html'


def conf_del_shop(request, pk):
    shop = get_object_or_404(models.Shop, pk=pk)
    return render(request, 'conf_del_shop.html', {'shop': shop})


def sign_out(request):  # выход из учетной записи
    logout(request)
    return redirect('main')


def sign_up(request):  # регистрация
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='client'))
            login(request, new_user)
            return redirect('client_main')
        else:
            return render(request, 'sign_up.html', {'form': form})
    else:
        form = forms.CreateUserForm()
        return render(request, 'sign_up.html', {'form': form})


def sign_in(request):  # авторизация
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            if is_manager(user):
                return redirect('admin_edit')
            else:
                return redirect('client_main')
        else:
            return render(request, 'sign_in.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'sign_in.html', {'form': form})


def is_manager(user):
    return user.groups.filter(name='manager').exists()


def client_main(request):
    return render(request, 'client_main.html')


def cake_create(request):
    if request.method == 'POST':
        form = forms.CakeForm(request.POST, request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.price = cake.weight * 1000
            cake.prepayment = cake.price / 2
            cake.client = request.user
            cake.save()
            return redirect('cakes')

        else:
            return redirect('cake_create')
    else:
        form = forms.CakeForm()
    return render(request, 'cake_create.html', {'form': form})


def cake_update(request, pk):
    cake = get_object_or_404(models.Cake, pk=pk)
    if request.method == 'POST':
        form = forms.UpdateCakeForm(request.POST, request.FILES, instance=cake)
        if form.is_valid():
            form.save()
            return redirect('cakes')
    else:
        form = forms.UpdateCakeForm(instance=cake)
    return render(request, 'cake_update.html', {'form': form})


def cakes(request):  # список заказов
    user = request.user
    if user.groups.filter(name='client').exists():
        is_client = True
        queryset = models.Cake.objects.filter(client=request.user)
    else:
        is_client = False
        queryset = models.Cake.objects.all
    return render(request, 'cakes.html', {'cakes': queryset, 'is_client': is_client})


def cake_detail(request, cake_id):  # детали заказа
    cake = get_object_or_404(models.Cake, pk=cake_id)
    return render(request, 'cake_detail.html', {'cake': cake})


class CakeUpdateView(UpdateView):
    model = models.Cake
    form_class = forms.CakeForm
    template_name = 'cake_update.html'
    success_url = reverse_lazy('cakes')


class CakeDeleteView(DeleteView):
    model = models.Cake
    success_url = reverse_lazy('cakes')
    template_name = 'cakes.html'


def confirm_delete_cake(request, pk):  # подтверждение удаления заказа
    cake = get_object_or_404(models.Cake, pk=pk)
    if (cake.date_ready - datetime.date.today()).days >= 1:
        return render(request, 'confirm_delete_cake.html', {'cake': cake})  # Вы действительно хотите удалить заказ?
    else:
        return render(request, 'fail_delete_cake.html', {'cake': cake})  # Вы не можете удалить заказ, потому что до
        # даты заказа осталось менее суток!
