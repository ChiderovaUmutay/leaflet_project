from rest_framework.viewsets import ModelViewSet

from webapp.models import Region
from webapp.serializer import RegionSerializer


class RegionViewSet(ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
