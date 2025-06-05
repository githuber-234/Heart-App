from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the User model
    name = models.CharField(max_length=25, default=user)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    Chest_Pain_Type = models.CharField(max_length=4, choices=[
        ('TA', 'Typical Angina'),
        ('ATA', 'Atypical Angina'),
        ('NAP', 'Non-Anginal Pain'),
        ('ASY', 'Asymptomatic'),
    ])
    restingBP = models.PositiveIntegerField()
    cholesterol = models.PositiveIntegerField()
    fastingBS = models.CharField(max_length=20, choices=[
        ('Less than 120', 'Less than 120mg/dL'),
        ('Greater than 120', 'Greater than 120mg/dL'),
    ])
    restingECG = models.CharField(max_length=10, choices=[
        ('Normal', 'Normal'),
        ('ST', 'ST-T Wave Abnormality'),
        ('LVH', 'Left Ventricular Hypertrophy'),
    ])
    maxHR = models.PositiveIntegerField()
    exercise_angina = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    oldpeak = models.DecimalField(max_digits=4, decimal_places=1)
    st_slope = models.CharField(max_length=10, choices=[
        ('Up', 'Upsloping'),
        ('Flat', 'Flat'),
        ('Down', 'Downsloping'),
    ])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assessment for {self.user.username}"
