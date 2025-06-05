from django.urls import path
from .views import download_assessment_data
from . import views

urlpatterns = [
    path('', views.home, name='heart_system-home'),
    path('assessment/', views.assessment, name='heart_system-assessment'),
    path('patienthistory/', views.patienthistory, name='heart_system-patienthistory'),
    path('healthTrends/', views.healthTrends, name='heart_system-healthTrends'),
    path('success/', views.success, name='heart_system-success'),
    path('download-assessment/', download_assessment_data, name='download_assessment'),
]
