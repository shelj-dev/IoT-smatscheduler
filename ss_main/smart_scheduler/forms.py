from django import forms
from smart_scheduler.models import Manual,Motion

from django.contrib.auth.forms import AuthenticationForm


class ManualForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = ["onTime", "offTime", "status"]
        widgets = {
            "onTime": forms.TimeInput(attrs={"type": "time"}),
            "offTime": forms.TimeInput(attrs={"type": "time"}),
        }


class MotionForm(forms.ModelForm):
    class Meta:
        model=Motion
        fields=['threshold','offDelay','status']

class LoginForm(AuthenticationForm):
    pass