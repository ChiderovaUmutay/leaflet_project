from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webapp.views import PlotView, AreaView, RegionViewSet

router = DefaultRouter()
router.register("regions", RegionViewSet)

urlpatterns = [
    path("area/<int:pk>/plot/add/", PlotView.as_view()),
    path("plot/<int:pk>/", PlotView.as_view()),
    path("region/<int:pk>/area/add/", AreaView.as_view()),
    path("area/<int:pk>/", AreaView.as_view()),
    path("", include(router.urls))
]
