from http import HTTPStatus

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Area, Plot
from webapp.serializer import PlotSerializer
from webapp.views.views_secondary_functions import get_serializer_data


class PlotView(APIView):
    serializer_class = PlotSerializer

    def post(self, request, *args, **kwargs):
        area = get_object_or_404(Area, pk=kwargs.get("pk"))
        new_plot = Plot.objects.create(**request.data, area=area)
        plot_serializer_data = get_serializer_data(new_plot, area, related_object_field="area")
        serializer = self.serializer_class(plot_serializer_data).data
        return Response(serializer, status=HTTPStatus.CREATED)

    def put(self, request, *args, pk, **kwargs):
        plot = get_object_or_404(Plot, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=plot)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.FOUND)

    def delete(self, request, *args, pk, **kwargs):
        plot = get_object_or_404(Plot, pk=pk)
        plot.delete()
        return Response({"message": "Поле успешно удалено"}, status=HTTPStatus.NO_CONTENT)
