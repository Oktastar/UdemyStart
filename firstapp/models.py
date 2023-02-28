from django.db import models


class PizzaShop(models.Model):  # первичная модель
    name = models.CharField(max_length=24, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Сайт пиццерии')

    class Meta:  # чтобы в админке не отображалось с s на конце
        verbose_name = 'Пиццерия'
        verbose_name_plural = 'Пиццерии'
        ordering = ['name']

# В админке не отображается имя пиццерии, описан просто объект.

    def __str__(self):
        return self.name


class Pizza(models.Model):  # вторичная модель
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    pizza_name = models.CharField(max_length=32, verbose_name='Название пиццы')
    short_description = models.CharField(max_length=64, verbose_name='Краткое описание')
    price = models.IntegerField(default=0, verbose_name='Цена')

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['pizza_name']  #  в админке по алфавиту

    def __str__(self):
        return self.pizza_name
