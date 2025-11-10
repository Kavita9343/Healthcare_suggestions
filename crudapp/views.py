from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
import csv, os
from django.conf import settings

# Load CSV to dictionary
def load_suggestions():
    filepath = os.path.join(settings.BASE_DIR, "symptom_suggestions.csv")
    suggestions = {}
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row["symptom"].lower().replace('"', '').strip()
            value = row["suggestion"].replace('"', '').strip()
            suggestions[key] = value
    return suggestions

def match_suggestion(symptoms):
    data = load_suggestions()
    symptoms = symptoms.lower()

    for symptom_list, suggestion in data.items():
        symptom_list = symptom_list.lower()
        if any(s.strip() in symptom_list for s in symptoms.split(",")):
            return suggestion
    
    return "Im not aware of it.Please consult a doctor!"
@login_required(login_url="/login/")
def index(request):
    patients = Patient.objects.filter(user=request.user)
    return render(request, "index.html", {"patients": patients})

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user   # ✅ store who created
            patient.suggestion = match_suggestion(patient.symptoms)
            patient.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, "add.html", {"form": form})

def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if patient.user != request.user:
        return HttpResponse("Unauthorized", status=401)
    
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.suggestion = match_suggestion(patient.symptoms)
            patient.save()
            return redirect('home')
    else:
        form = PatientForm(instance=patient)
    return render(request, "edit.html", {"form": form})

def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    
    if patient.user != request.user:
        return HttpResponse("Unauthorized", status=401)

    
    patient.delete()
    return redirect('home')



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect("login")  

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  
        else:
            messages.error(request,'Invalid username or password!')
            
    return render(request, "login.html")
