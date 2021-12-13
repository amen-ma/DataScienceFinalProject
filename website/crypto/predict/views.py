from django.shortcuts import render
from django.http import JsonResponse
#import pandas as pd
#from .models import PredResults



# Create your views here.

def predict(request):
    return render(request, 'predict.html')

