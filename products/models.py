from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name