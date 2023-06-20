from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рестораны'


class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name='Ресторан')
    number = models.CharField(max_length=10, verbose_name='Номер')
    capacity = models.PositiveIntegerField(
        verbose_name='Вместимость')
    reservations = models.ManyToManyField(
        User, through='Reservation', verbose_name='Резервации')

    def __str__(self):
        return f"Table {self.number} at {self.restaurant.name}"

    class Meta:
        verbose_name_plural = 'Столики'


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, verbose_name='Столик')
    date = models.DateField(verbose_name='Дата')
    start_time = models.TimeField(
        verbose_name='Начало')
    end_time = models.TimeField(verbose_name='Конец')

    def __str__(self):
        return f"Reservation by {self.user.username} at {self.table.restaurant.name}"

    class Meta:
        verbose_name_plural = 'Резервации'


class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name='Ресторан')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.PositiveIntegerField(verbose_name='Рейтинг')
    comment = models.TextField(verbose_name='Комментарий')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f"Review by {self.user.username} for {self.restaurant.name}"

    class Meta:
        verbose_name_plural = 'Отзывы'


class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name='Ресторан')
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Пункты меню'


class Staff(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name='Ресторан')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    position = models.CharField(max_length=255, verbose_name='Должность')
    contact_number = models.CharField(max_length=20, verbose_name='Контактный номер')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Персонал'
