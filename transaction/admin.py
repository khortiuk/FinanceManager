from django.contrib import admin
from .models import Operation, Transaction


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'operation_type', 'amount', 'date']
