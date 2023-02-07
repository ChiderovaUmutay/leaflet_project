from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Region, Area
from webapp.serializer import AreaSerializer
from webapp.views.views_secondary_functions import get_serializer_data


class AreaView(APIView):
    serializer_class = AreaSerializer

    def post(self, request, *args, **kwargs):
        region = get_object_or_404(Region, pk=kwargs.get("pk"))
        new_area = Area.objects.create(**request.data, region=region)
        area_serializer_data = get_serializer_data(new_area, region, related_object_field="region")
        serializer = self.serializer_class(area_serializer_data).data
        return Response(serializer)

    def put(self, request, *args, pk, **kwargs):
        area = get_object_or_404(Area, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=area)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, pk, **kwargs):
        area = get_object_or_404(Area, pk=pk)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        area.delete()
        return Response({"message": "Район успешно удален"})
