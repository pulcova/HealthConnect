from django.urls import path
from .views import patient_list, patient_detail, patient_create

app_name = "patients"

urlpatterns = [
    path('', patient_list),
    path('create/', patient_create),
    path('<int:pk>/', patient_detail),
]
