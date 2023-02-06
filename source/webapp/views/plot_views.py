from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Area, Plot
from webapp.serializer import PlotSerializer
from webapp.views.views_secondary_functions import get_serializer_data


class PlotAdd(APIView):
    plot_serializer_class = PlotSerializer

    def post(self, request, *args, **kwargs):
        area = get_object_or_404(Area, pk=kwargs.get("pk"))
        new_plot = Plot.objects.create(**request.data, area=area)
        plot_serializer_data = get_serializer_data(new_plot, area, related_object_field="area")
        serializer = self.plot_serializer_class(plot_serializer_data).data
        return Response(serializer)
