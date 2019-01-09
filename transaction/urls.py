from django.urls import path
from .views import TransactionListView, TransactionCreateView, TransactionDetailView, TransactionDeleteView

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('<int:pk>', TransactionDetailView.as_view(), name='transaction_detail'),
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('new/', TransactionCreateView.as_view(), name='transaction_create')
]
