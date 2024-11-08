from django.db import models
import datetime


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, verbose_name="Производитель")

    class Meta:
        verbose_name_plural = "Производители"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name="Страна")

    class Meta:
        verbose_name_plural = "Страны"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название города")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} {self.country}'

    class Meta:
        verbose_name_plural = "Города"
        ordering = ['name']


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name="Магазины")
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    adress = models.CharField(max_length=50, verbose_name="Адрес")

    class Meta:
        verbose_name_plural = "Магазины"
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.city} {self.adress}'


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name="Статус наличия товара")

    class Meta:
        verbose_name_plural = "Статус наличия товара"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name="Статус заказа")

    class Meta:
        verbose_name_plural = "Статус заказа"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Form(models.Model):
    name = models.CharField(max_length=50, verbose_name="Форма торта")

    class Meta:
        verbose_name_plural = "Форма торта"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Tier(models.Model):
    name = models.CharField(max_length=50, verbose_name="Количество ярусов торта (этажей)")

    class Meta:
        verbose_name_plural = "Количество ярусов торта (этажей)"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Filling(models.Model):
    name = models.CharField(max_length=50, verbose_name="Начинка")

    class Meta:
        verbose_name_plural = "Начинка"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Good(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование ингредиента")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена,сом/кг")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(verbose_name='Количество,кг')
    photo = models.ImageField(upload_to='cakes/', null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} {self.manufacturer}'

    class Meta:
        verbose_name_plural = "Ингредиенты"
        ordering = ['name']


class Cake(models.Model):
    form = models.ForeignKey(Form, on_delete=models.DO_NOTHING, verbose_name="Форма торта")
    tier = models.ForeignKey(Tier, on_delete=models.DO_NOTHING, verbose_name="Количество ярусов торта (этажей)")
    filling = models.ForeignKey(Filling, on_delete=models.DO_NOTHING, verbose_name="Начинка")
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Вес торта")
    photo = models.ImageField(upload_to='media/cakes/', null=True, blank=True, verbose_name="Приложите фото торта, который вам нравится")
    color = models.CharField(max_length=30, default='', verbose_name="Основная цветовая гамма")
    inscription = models.CharField(max_length=50, verbose_name="Надпись на торте")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена торта, сом', default=0.00)
    prepayment = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Предоплата 50%')
    date_create = models.DateField(verbose_name='Дата создания заказа', default=datetime.date.today())
    date_ready = models.DateField(verbose_name='Дата выдачи торта', default=datetime.date.today())
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING, default=1, verbose_name='Статус заказа')
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, default=1, verbose_name='Магазин для получения торта')
    comments = models.CharField(max_length=250, default='', verbose_name="Комментарии")
    client_name = models.CharField(max_length=30, default='', verbose_name="Имя клиента")
    phone_number = models.CharField(max_length=30, default='', verbose_name="Номер телефона")
    client = models.TextField(verbose_name='Заказчик',default='')

    def __str__(self):
        return f'{self.form} {self.tier} {self.filling} {self.weight}'

    class Meta:
        verbose_name_plural = "Торты"
        ordering = ['filling']

