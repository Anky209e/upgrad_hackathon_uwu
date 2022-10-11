from django.shortcuts import render,redirect
from .forms import FakeNewsForm

def fakenews(request):
# Create your views here.
    context = {}
    form = FakeNewsForm(request.POST)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request, 'fakenews.html', context)