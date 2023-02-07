import factory

from webapp.models import Area, Plot, Region


class RegionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Region

    class Params:
        with_conversion_rate = factory.Trait(
            conversion_rate=factory.RelatedFactory('webapp.tests.factories.AreaFactory', 'region'),
        )

    name = factory.Faker("name")
    coordinates = factory.Sequence(lambda
                                       n: f'SRID=32140;LINESTRING (11479798.195462396 6789130.838130293, 11543214.96529969 6834626.161989568, 11509026.745469585 6765665.943992906, 11479771.289860094 6788388.403652353)')
    # with_conversion_rate = True


class AreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Area

    class Params:
        with_conversion_rate = factory.Trait(
            conversion_rate=factory.RelatedFactory('webapp.tests.factories.PlotFactory', 'area'),
        )

    name = factory.Faker("name")
    coordinates = factory.Sequence(lambda
                                       n: f'SRID=32140;LINESTRING (11479798.195462396 6789130.838130293, 11543214.96529969 6834626.161989568, 11509026.745469585 6765665.943992906, 11479771.289860094 6788388.403652353)')
    region = factory.SubFactory(
        RegionFactory,
        with_conversion_rate=False,
    )


class PlotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Plot

    name = factory.Faker("name")
    coordinates = factory.Sequence(lambda
                                       n: f'SRID=32140;LINESTRING (11479798.195462396 6789130.838130293, 11543214.96529969 6834626.161989568, 11509026.745469585 6765665.943992906, 11479771.289860094 6788388.403652353)')

    area = factory.SubFactory(
        AreaFactory,
        with_conversion_rate=False,
    )
