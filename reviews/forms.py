from django import forms
from reviews.models import Review


RATING_CHOICES = [(i, str(i)) for i in range(6)]  # Creates a list of tuples for ratings from 0 to 5

class ReviewForm(forms.ModelForm):
    
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))
    rating = forms.ChoiceField(choices=RATING_CHOICES)
    
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']