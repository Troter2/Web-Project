from django.shortcuts import render
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def new_review(request):
    if request.method == 'POST':
        return render(request, 'review/review_2.html')
    else:
        review_form = ReviewForm()
    return render(request, 'review/review_1.html', {'review_form': review_form})
