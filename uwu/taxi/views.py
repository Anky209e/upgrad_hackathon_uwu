from django.shortcuts import render,redirect
from matplotlib.style import context
from .forms import TaxiForm
from .models import Taxi
# Create your views here.
def home(request):
    
    context = {}
    form = TaxiForm(request.POST)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request, 'home.html', context)