from django.shortcuts import render
from .forms import Sdata
from .models import Edata

# Create your views here.


def home(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('location') and request.POST.get('dob'):
            edata = Edata()
            edata.name = request.POST.get('name')
            edata.location = request.POST.get('location')
            edata.dob = request.POST.get('dob')
            edata.save()

            return render(request,'home.html')
    else:

        return render(request, "home.html")
