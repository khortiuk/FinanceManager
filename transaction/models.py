from django.db import models

from category.models import Category


class Operation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    operation_type = models.ForeignKey(Operation, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    short_description = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)

    @property
    def category_name(self):
        return self.category.title
