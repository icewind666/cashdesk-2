# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    fileLink = forms.FileField(
        label='Select a file',
    )