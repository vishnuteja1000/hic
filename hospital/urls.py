from django.urls import path,include
from . import views

urlpatterns = [
    path(route='hospitalsdata/',view= views.getHospitals, name='allhospitals')
]