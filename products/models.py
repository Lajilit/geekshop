from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Наименование',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
    )


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Наименование',
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
        verbose_name='Изображение',
    )
    description = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Описание',
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Цена',
    )
    quantity = models.PositiveIntegerField(
        default=2,
        verbose_name='Количество',
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
