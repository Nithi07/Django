from django.shortcuts import render
from .forms import Sdata
from .models import Edata

# Create your views here.


def home(request):
    det = Sdata()
    return render(request, "home.html",{'det':det})
