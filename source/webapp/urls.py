from django.urls import path

from webapp.views import PlotAdd, AreaAdd

urlpatterns = [
    path("area/<int:pk>/plot/add/", PlotAdd.as_view()),
    path("region/<int:pk>/area/add/", AreaAdd.as_view())
]