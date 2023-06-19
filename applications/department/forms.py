from django import forms

class NewDepartmentForm(forms.Form):
    name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    name_deparment = forms.CharField(max_length=15)
    short_name = forms.CharField(max_length=15)