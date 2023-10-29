from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields ='__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; margin: 10px 0',
                'placeholder': 'Course title'
                }),
            'Description': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; margin: 10px 0',
                'placeholder': 'Course title'
                }),
            'link': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; margin: 10px 0',
                'placeholder': 'Course title'
                }),
            'image': forms.FileInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; margin: 10px 0',
                'placeholder': 'Course title'
                })
        }