# -*- coding: utf-8 -*-

from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'hiragana_name',
            'distance',
            'event',
            'time_min',
            'time_sec',
            'created_at',
            'memo',
        ]