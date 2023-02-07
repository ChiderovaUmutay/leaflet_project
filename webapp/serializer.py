from rest_framework_gis import serializers

from webapp.models import Plot, Area, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "name", "coordinates")


class AreaSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = Area
        fields = ("id", "name", "coordinates", "region")


class PlotSerializer(serializers.ModelSerializer):
    area = AreaSerializer(read_only=True)

    class Meta:
        model = Plot
        fields = ("id", "name", "coordinates", "area")
