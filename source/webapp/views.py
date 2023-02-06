# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Area, Plot, Region
from webapp.serializer import PlotSerializer, AreaSerializer

serializer_data = {}


def get_serializer_data(obj, related_object, related_object_field=None):
    serializer_data["id"] = obj.id
    serializer_data["name"] = obj.name
    serializer_data["coordinates"] = obj.coordinates
    if related_object_field:
        serializer_data[related_object_field] = related_object
    return serializer_data


class PlotAdd(APIView):
    plot_serializer_class = PlotSerializer

    def post(self, request, *args, **kwargs):
        area = get_object_or_404(Area, pk=kwargs.get("pk"))
        new_plot = Plot.objects.create(**request.data, area=area)
        plot_serializer_data = get_serializer_data(new_plot, area, related_object_field="area")
        serializer = self.plot_serializer_class(plot_serializer_data).data
        return Response(serializer)


class AreaAdd(APIView):
    area_serializer_class = AreaSerializer

    def post(self, request, *args, **kwargs):
        region = get_object_or_404(Region, pk=kwargs.get("pk"))
        new_area = Area.objects.create(**request.data, region=region)
        area_serializer_data = get_serializer_data(new_area, region, related_object_field="region")
        serializer = self.area_serializer_class(area_serializer_data).data
        return Response(serializer)

