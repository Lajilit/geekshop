from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')