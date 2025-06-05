from django.shortcuts import render, redirect
from .models import Assessment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import csv
from django.http import HttpResponse
from .models import Assessment

def home(request):
    return render(request, 'heart_system/home.html')

@login_required
def assessment(request):
    user = request.user

    if request.method == "POST":
        # Retrieve form data from the submitted request
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        Chest_Pain_Type = request.POST.get('chestPainType')
        restingBP = request.POST.get('restingBP')
        cholesterol = request.POST.get('cholesterol')
        fastingBS = request.POST.get('fastingBS')
        restingECG = request.POST.get('restingECG')
        maxHR = request.POST.get('maxHR')
        exercise_angina = request.POST.get('exerciseAngina')
        oldpeak = request.POST.get('oldpeak')
        st_slope = request.POST.get('stSlope')

        # Save the data to the database
        Assessment.objects.create(
            user=user,
            name=name,
            age=age,
            sex=sex,
            Chest_Pain_Type=Chest_Pain_Type,
            restingBP=restingBP,
            cholesterol=cholesterol,
            fastingBS=fastingBS,
            restingECG=restingECG,
            maxHR=maxHR,
            exercise_angina=exercise_angina,
            oldpeak=oldpeak,
            st_slope=st_slope,
        )

        return redirect('heart_system-success')

    user_assessments = Assessment.objects.filter(user=user)
    return render(request, 'heart_system/assessment.html', {'user_assessments': user_assessments})

@login_required
def patienthistory(request):
    user = request.user
    user_assessments = Assessment.objects.filter(user=user)
    return render(request, 'heart_system/patienthistory.html', {'user_assessments': user_assessments})


def healthTrends(request):
    return render(request, 'heart_system/healthTrends.html')

def success(request):
    return render(request, 'heart_system/success.html')

def download_assessment_data(request):
    user = request.user

    # Create an HTTP response with CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assessment_data.csv"'

    writer = csv.writer(response)
    
    writer.writerow([
        'User', 'Name', 'Age', 'Sex', 'Chest Pain Type', 'Resting BP', 
        'Cholesterol', 'Fasting BS', 'Resting ECG', 'Max HR', 
        'Exercise Angina', 'Oldpeak', 'ST Slope', 'Created At'
    ])

    assessments = Assessment.objects.filter(user=user)

    # Write data rows
    for assessment in assessments:
        writer.writerow([
            assessment.user.username,  # Or assessment.user.id
            assessment.name,
            assessment.age,
            assessment.sex,
            assessment.Chest_Pain_Type,
            assessment.restingBP,
            assessment.cholesterol,
            assessment.fastingBS,
            assessment.restingECG,
            assessment.maxHR,
            assessment.exercise_angina,
            assessment.oldpeak,
            assessment.st_slope,
            assessment.date_created, 
        ])

    return response