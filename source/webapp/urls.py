from django.urls import path

from webapp.views import PlotAdd

urlpatterns = [
    path('area/<int:pk>/plot/add/', PlotAdd.as_view()),
]
