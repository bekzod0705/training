from django.urls import path
from .views import message
urlpatterns=[
    path('all/<int:forid>/',message)
]