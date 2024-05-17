from django import forms
from reviews.models import Review


RATING_CHOICES = [(i, str(i)) for i in range(6)]
PRODUCTION_CHOICES = [('Movie', 'Movie'), ('Serie', 'Serie')]

class ReviewForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}), label='Content')
    rating = forms.ChoiceField(choices=RATING_CHOICES, label='Rating', required=False)

    class Meta:
        model = Review
        fields = ['content', 'rating']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not rating:
            return str(0)
        return rating