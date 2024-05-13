from django import forms
from reviews.models import Review


RATING_CHOICES = [(i, str(i)) for i in range(6)]
PRODUCTION_CHOICES = [('Movie', 'Movie'), ('Serie', 'Serie')]

class ReviewForm(forms.ModelForm):
    

    production_type= forms.ChoiceField(choices=PRODUCTION_CHOICES, label='Production')
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}), label='Content')
    rating = forms.ChoiceField(choices=RATING_CHOICES, label='Rating')
    
    class Meta:
        model = Review
        fields = ['content', 'rating', 'production_type']