from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class PSOSettingForm(forms.Form):
    particle_number = forms.IntegerField(initial=500, min_value=20, max_value=500)
    iteration_number = forms.IntegerField(initial=10, max_value=100)
    inertia_weight = forms.FloatField(initial=0.5, min_value=0)
    cognitive_constant = forms.FloatField(initial=2.04, min_value=0)
    social_constant = forms.FloatField(initial=2.04, min_value=0)
    initial_position = forms.CharField(initial="random")
