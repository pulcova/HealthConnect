from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient, Doctor
from .forms import PatientForm

def patient_list(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients
    }
    return render(request, "patients/patient_list.html", context)

def patient_detail(request, pk):
    patient = Patient.objects.get(id=pk)
    context = {
        "patient": patient
    }
    patient = Patient.objects.get(id=pk)
    return render(request, "patients/patient_detail.html", context)

def patient_create(request):
    form = PatientForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = PatientForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            doctor = Doctor.objects.first()
            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                doctor=doctor,
            )
            return redirect("/patients")
    context = {
        "form": form
    }
    return render(request, "patients/patient_create.html", context)