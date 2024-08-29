from django import forms
from .models import ad


class AdForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=255, required=False, help_text="Enter comma-separated tags"
    )

    description = forms.CharField(max_length=2000, required=True, widget=forms.Textarea)

    class Meta:
        model = ad
        fields = ["title", "category", "location", "tags", "description"]
