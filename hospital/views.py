from django.shortcuts import render
from .models import Hospital,Hospital_Type

# Create your views here.
def getHospitals(request):
    all_hospitals=Hospital.objects.all()
    return render(request,'hospitals.html', {'all_hospitals_key':'all_hospitals'})
