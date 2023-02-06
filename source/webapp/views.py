# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Area, Plot
from webapp.serializer import PlotSerializer


class PlotAdd(APIView):
    serializer_class = PlotSerializer
    serializer_data = {}

    def get_serializer_data(self, plot, area):
        self.serializer_data["id"] = plot.id
        self.serializer_data["name"] = plot.name
        self.serializer_data["coordinates"] = plot.coordinates
        self.serializer_data["area"] = area

    def post(self, request, *args, **kwargs):
        area = get_object_or_404(Area, pk=kwargs.get("pk"))
        new_plot = Plot.objects.create(**request.data, area=area)
        self.get_serializer_data(new_plot, area)
        serializer = self.serializer_class(self.serializer_data).data
        return Response(serializer)
