from django import forms
from .models import Task
from contractors.models import Contractor  # Import Contractor

class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=Contractor.objects.all(), required=False, label="Assign Contractor")  # Updated

    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'assigned_to', 'due_date', 'status']