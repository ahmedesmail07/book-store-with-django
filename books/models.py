from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # def __str__(self):
    #     return f"{self.title} by {self.author}"
    # use it if u will not use list_display in admin.py
