from django import forms

class ProjectForm(forms.Form):
    projectName = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Enter projectName'
        }))