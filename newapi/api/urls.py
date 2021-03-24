from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('athlete-list/', views.athleteList, name='athlete-list'),
    path('athlete-create/', views.athleteCreate, name='athlete-create')
]