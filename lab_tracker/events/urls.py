from django.urls import path
from . import views

urlpatterns= [
    path('', views.ongoing_events, name= 'ongoing_events'),
    path('past_events', views.past_events, name= 'past_events'),
    path('upcoming_events', views.upcoming_events, name= 'upcoming_events'),

    path('event_page/', views.event_page, name= 'event_page'),

]
 