from django import forms
from .models import *


class RallyForm(forms.ModelForm):
    class Meta:
        model = Rally
        fields = '__all__'


class PublicGatheringForm(forms.ModelForm):
    class Meta:
        model = PublicGathering
        fields = '__all__'


class NaturalCalamitiesForm(forms.ModelForm):
    class Meta:
        model = NaturalCalamities
        fields = '__all__'


class EpidemicForm(forms.ModelForm):
    class Meta:
        model = Epidemic
        fields = '__all__'


class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = '__all__'



