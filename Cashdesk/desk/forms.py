# -*- coding: utf-8 -*-
from django import forms


class DocumentForm(forms.Form):
    fileLink = forms.FileField(
        label='Select a file'
    )
    company = forms.CharField(widget=forms.HiddenInput())


class EditDocumentForm(forms.Form):
    op_file = forms.FileField(
        label='Select a file',
        required=False
    )
    op_id = forms.CharField(widget=forms.HiddenInput())
    op_company = forms.CharField(widget=forms.HiddenInput())
