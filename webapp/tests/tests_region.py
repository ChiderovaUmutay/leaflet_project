from http import HTTPStatus

from rest_framework.test import APITestCase

from webapp.factories.factories import RegionFactory
from webapp.models import Region


class RegionTest(APITestCase):
    def test_region_add(self):
        data = {"name": "TestRegion",
                "coordinates": "LINESTRING (11714907.412591541 7347786.87314456, 11804942.41252233 7379764.893450736, 11738722.988848228 7300546.390507504, 11715352.856542937 7346910.6920190975)"}
        response = self.client.post("/regions/", data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        region = Region.objects.filter(name="TestRegion")
        self.assertEqual(len(region), 1)

    def test_region_update(self):
        region = RegionFactory()
        response = self.client.put(f"/regions/{region.pk}/",
                                   {"name": "UpdateTestRegion",
                                    "coordinates": "LINESTRING (11714907.412591541 7347786.87314456, 11804942.41252233 7379764.893450736, 11738722.988848228 7300546.390507504, 11715352.856542937 7346910.6920190975)"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        region = Region.objects.filter(name="UpdateTestRegion")
        self.assertEqual(len(region), 1)

    def test_region_delete(self):
        region = RegionFactory()
        response = self.client.delete(f"/regions/{region.pk}/")
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        region = Region.objects.filter(id=region.id)
        self.assertEqual(len(region), 0)
