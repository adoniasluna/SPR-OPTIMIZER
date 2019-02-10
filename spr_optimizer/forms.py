from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class PSOSettingForm(forms.Form):
    particle_number = forms.IntegerField(initial=500)
    iteration_number = forms.IntegerField(initial=10)
    inertia_weight = forms.FloatField(initial=2)
    group_nostalgia = forms.FloatField(initial=500)
    individual_nostalgia = forms.IntegerField(initial=500)
    initial_position = forms.CharField(initial="random")

    def clean_particle_number(self):
        data = self.cleaned_data['particle_number']

        if data <= 0 or data > 1000:
            raise ValidationError(_('Invalid number of particles'))

        return data

    def clean_iteration_number(self):
        data = self.cleaned_data['iteration_number']

        if data <= 0 or data > 100:
            raise ValidationError(_('Invalid number iterations'))
        return data
