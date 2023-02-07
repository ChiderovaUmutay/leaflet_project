from http import HTTPStatus

from rest_framework.test import APITestCase

from webapp.factories.factories import AreaFactory, RegionFactory
from webapp.models import Area


# Create your tests here.
class AreaTest(APITestCase):

    def test_area_add(self):
        region = RegionFactory()
        data = {"name": "TestArea",
                "coordinates": "LINESTRING (11714907.412591541 7347786.87314456, 11804942.41252233 7379764.893450736, 11738722.988848228 7300546.390507504, 11715352.856542937 7346910.6920190975)"}
        response = self.client.post(f"/region/{region.pk}/area/add/", data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        area = Area.objects.filter(name="TestArea")
        self.assertEqual(len(area), 1)

    def test_area_update(self):
        area = AreaFactory()
        response = self.client.put(f"/area/{area.pk}/",
                                   {"name": "UpdateTestArea",
                                    "coordinates": "LINESTRING (11714907.412591541 7347786.87314456, 11804942.41252233 7379764.893450736, 11738722.988848228 7300546.390507504, 11715352.856542937 7346910.6920190975)"})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        area = Area.objects.filter(name="UpdateTestArea")
        self.assertEqual(len(area), 1)

    def test_area_delete(self):
        area = AreaFactory()
        response = self.client.delete(f"/area/{area.pk}/")
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        area = Area.objects.filter(id=area.id)
        self.assertEqual(len(area), 0)
