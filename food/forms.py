from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from .models import foods
class foodform(forms.ModelForm):
    class Meta:
        model= foods
        fields=['name','des','desc']