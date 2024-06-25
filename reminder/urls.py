from django.urls import path

from . import views


urlpatterns = [
    path('persons/', views.PersonView.as_view()),
    path('persons/<int:person_id>/', views.PersonUpdateDeleteView.as_view()),

    path('events/', views.EventView.as_view()),
]
