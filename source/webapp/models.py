from django.contrib.gis.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название региона")
    coordinates = models.GeometryField(srid=32140, verbose_name="Координаты региона")
    areas = models.ManyToManyField("webapp.Area", related_name="region_areas",
                                   verbose_name="Районы")

    def __str__(self):
        return f"Регион {self.name}"

    class Meta:
        db_table = "regions"
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название района")
    coordinates = models.GeometryField(srid=32140, verbose_name="Координаты района")
    plots = models.ManyToManyField("webapp.Plot", related_name="area_plots",
                                   verbose_name="Поля")

    def __str__(self):
        return f"Район {self.name}"

    class Meta:
        db_table = "areas"
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Plot(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название поля")
    coordinates = models.GeometryField(srid=32140, verbose_name="Координаты поля")

    def __str__(self):
        return f"Поле {self.name}"

    class Meta:
        db_table = "plots"
        verbose_name = "Поле"
        verbose_name_plural = "Поля"

