# athletics/forms.py
from django import forms
from .models import RaceResult, Race


class RaceResultForm(forms.ModelForm):
    class Meta:
        model = RaceResult
        fields = ['athlete', 'race', 'position']


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class SendEmailForm(forms.Form):
    race = forms.ModelChoiceField(queryset=Race.objects.all(), label="Select Race")
