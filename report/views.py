import datetime
import json

from django.db.models import Sum

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.views.generic import FormView, TemplateView

from .forms import ReportGenerateForm
from transaction.models import Transaction


class GenerateReportView(LoginRequiredMixin, FormView):
    form_class = ReportGenerateForm
    template_name = 'report/create_report.html'
    success_url = reverse_lazy('report')

    def post(self, request, *args, **kwargs):
        self.template_name = 'report/result.html'
        return super(GenerateReportView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GenerateReportView, self).get_context_data(**kwargs)
        objects = Transaction.objects.order_by('date')
        context['first_date'] = objects.first().date.date()
        # context['last_date'] = objects.last().date.date()
        return context


class ResultReportView(LoginRequiredMixin, TemplateView):
    template_name = 'report/result.html'
    login_url = 'sing-in'

    def get_context_data(self, **kwargs):
        context = super(ResultReportView, self).get_context_data(**kwargs)
        category = self.request.GET.get('category')
        operation = self.request.GET.get('operation')
        date_range = self.request.GET.get('date_range').split('-')
        context['s_date'] = date_range[0].strip().replace('/', '-')
        context['e_date'] = date_range[1].strip().replace('/', '-')
        res = list()
        for user in User.objects.all():
            res.append({
                'name': user.username,
                'y': float(Transaction.objects.filter(author=user,
                                                      category__id=category,
                                                      operation_type=operation,
                                                      date__range=(context['s_date'],
                                                                   context['e_date'])).aggregate(Sum('amount'))[
                               'amount__sum'] or 0)
            })
        context['series'] = json.dumps(res)
        return context
