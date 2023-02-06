from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Region
from webapp.serializer import RegionSerializer


class RegionAdd(APIView):
    region_serializer_class = RegionSerializer

    def post(self, request, *args, **kwargs):
        new_region = Region.objects.create(**request.data)
        serializer = self.region_serializer_class(new_region).data
        return Response(serializer)