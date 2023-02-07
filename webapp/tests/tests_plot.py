from http import HTTPStatus

from rest_framework.test import APITestCase

from webapp.factories.factories import AreaFactory, PlotFactory
from webapp.models import Plot


# Create your tests here.
class PlotTest(APITestCase):

    def test_plot_add(self):
        area = AreaFactory()
        data = {"name": "TestPlot",
                "coordinates": "LINESTRING (11714907.412591541 7347786.87314456, 11804942.41252233 7379764.893450736, 11738722.988848228 7300546.390507504, 11715352.856542937 7346910.6920190975)"}
        response = self.client.post(f"/area/{area.pk}/plot/add/", data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        plot = Plot.objects.filter(name="TestPlot")
        self.assertEqual(len(plot), 1)

    def test_plot_update(self):
        plot = PlotFactory()
        response = self.client.put(f"/plot/{plot.pk}/",
                                   {"name": "UpdateTestPlot",
                                    "coordinates": "LINESTRING (11714907.412591541 7347786.87314456, 11804942.41252233 7379764.893450736, 11738722.988848228 7300546.390507504, 11715352.856542937 7346910.6920190975)"})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        plot = Plot.objects.filter(name="UpdateTestPlot")
        self.assertEqual(len(plot), 1)

    def test_plot_delete(self):
        plot = PlotFactory()
        response = self.client.delete(f"/plot/{plot.pk}/")
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        plot = Plot.objects.filter(id=plot.id)
        self.assertEqual(len(plot), 0)
