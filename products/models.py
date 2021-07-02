from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='наименование',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='описание',
    )

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='наименование',
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
        verbose_name='изображение',
    )
    description = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='описание',
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='цена',
    )
    quantity = models.PositiveIntegerField(
        default=2,
        verbose_name='количество',
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )

    class Meta():
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
