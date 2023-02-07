from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from webapp.models import Region
from webapp.serializer import RegionSerializer


class RegionViewSet(ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    # def post(self, request, *args, **kwargs):
    #     new_region = Region.objects.create(**request.data)
    #     serializer = self.region_serializer_class(new_region).data
    #     return Response(serializer)