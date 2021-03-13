from django import forms
from .models import photo

class ImageForm(forms.ModelForm):
    class Meta:
        model = photo
        fields = '__all__'
        labels = {'photo':''}