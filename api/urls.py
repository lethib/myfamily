from django.urls import path
from .views import people, family

urlpatterns = [
    path("people", people.index, name="People Index"),
    path("people/<str:pk>", people.show, name="People Show"),
    path("families", family.index, name="Families"),
    path("families/<str:pk>", family.show, name="Family"),
]
