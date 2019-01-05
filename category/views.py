from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryCreateForm


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categorys'
    login_url = 'sing-in'


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'category/category_create.html'
    login_url = 'sing-in'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'
    login_url = 'sing-in'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    login_url = 'sing-in'
