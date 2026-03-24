from django import forms
from smart_scheduler.models import ManualSchedule,Motion

from django.contrib.auth.forms import AuthenticationForm


class ManualScheduleForm(forms.ModelForm):
    class Meta:
        model = ManualSchedule
        fields = ["onTime", "offTime", "status"]
        widgets = {
            "onTime": forms.TimeInput(attrs={"type": "time"}),
            "offTime": forms.TimeInput(attrs={"type": "time"}),
        }


class MotionForm(forms.ModelForm):
    class Meta:
        model=Motion
        fields=['status']

class LoginForm(AuthenticationForm):
    pass

