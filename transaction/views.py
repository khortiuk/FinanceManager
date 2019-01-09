from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Transaction
from .forms import TransactionCreateForm


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'transaction/transaction_list.html'
    login_url = 'sing-in'


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'transaction/transaction_detail.html'
    login_url = 'sing-in'


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')
    login_url = 'sing-in'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionCreateForm
    template_name = 'transaction/transaction_create.html'
    login_url = 'sing-in'
    success_url = reverse_lazy('transaction_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(TransactionCreateView, self).form_valid(form)
