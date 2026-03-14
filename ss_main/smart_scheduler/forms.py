from django import forms
from smart_scheduler.models import Manual,Motion

class ManualForm(forms.ModelForm):
    class Meta:
        model=Manual
        fields=["onTime","offTime","status"]

class MotionForm(forms.ModelForm):
    class Meta:
        model=Motion
        fields=['theshold','offDelay','staus']