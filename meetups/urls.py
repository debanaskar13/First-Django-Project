from django.urls import path
from . import views

urlpatterns = [
    path('meetup/<slug:meetup_slug>/success', views.confirm_registration,name='confirm-registration'),
    path('meetups/<slug:meetup_slug>',views.meetup_details, name='meetup-details'),
    path('', views.index, name='all-meetups'),
]
