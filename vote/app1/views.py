from django.shortcuts import render,get_list_or_404
from .models import Poll,Choice
from django.db.models import Count,Sum
# Create your views here.

def home(request):
    vote_none=Choice.objects.filter(poll_id=1).aggregate(Count("poll_id"))
    vote_ai=Choice.objects.filter(poll_id=2).aggregate(Count('poll_id'))
    vote_ml=Choice.objects.filter(poll_id=3).aggregate(Count("poll_id"))
    print("ml:",vote_ml)
    context={'none':vote_none,'ai':vote_ai,'ml':vote_ml}
    return render(request,'app1/vote.html',context)
