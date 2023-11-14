from django.urls import path
from rcb.views import *

app_name = 'blank'

urlpatterns = [
    path('virat/',virat, name='virat'),
    path('abd/',abd, name='abd'),
]