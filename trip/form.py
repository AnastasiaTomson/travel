from django.forms import ModelForm
from django import forms

from .models import *
from django.forms.models import inlineformset_factory


class UserTripForm(forms.ModelForm):
    class Meta:
        model = UserTrip

        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.request_user
        return super().save(*args, **kwargs)


ChildrenFormset = inlineformset_factory(UserTrip, UserPlace, fields='__all__', can_delete=True, extra=0,
                                        widgets={
                                            'visit_date': forms.DateInput(attrs={'class': 'date'}, format='%d.%m.%Y'),
                                            'visit_time': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
                                            'place': forms.NumberInput(),
                                        })
