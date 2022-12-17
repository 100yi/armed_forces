from django.urls import path
from .views import *


urlpatterns = [
    path('', about, name='main'),
    path('about/', about, name='about'),
    path('all_schools/', all_schools, name='all_schools'),
    path('certain_school/<str:name>/', certain, name='certain'),
]
