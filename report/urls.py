from django.urls import path

from .views import GenerateReportView, ResultReportView

urlpatterns = [
    path('', GenerateReportView.as_view(), name='report'),
    path('result/', ResultReportView.as_view(), name='report_result')
]
