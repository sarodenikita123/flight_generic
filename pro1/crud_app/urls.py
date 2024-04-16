from django.urls import path
from .views import *

urlpatterns = [
    path('', FlightCreate.as_view()),
    path("list/", FlightList.as_view()),
    path("detail/<pk>/", FlightDetail.as_view()),
    path("update/<pk>/", FlightUpdate.as_view()),
    path("delete/<pk>/", FlightDelete.as_view()),

]
