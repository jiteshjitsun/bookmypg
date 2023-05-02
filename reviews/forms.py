from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = (
            "review",
            "accuracy",
            "communication",
            "cleanliness",
            "location",
            "value",
        )

    def save(self):
        review = super().save(commit=False)
        return review