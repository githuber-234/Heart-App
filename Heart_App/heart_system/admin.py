from django.contrib import admin
from .models import Assessment  # Import your model

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'age', 'sex','Chest_Pain_Type',
                    'restingBP', 'cholesterol', 'fastingBS', 
                    'restingECG', 'maxHR', 'exercise_angina',
                    'oldpeak', 'st_slope', 'date_created')
