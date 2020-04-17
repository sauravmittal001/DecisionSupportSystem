import rest_framework

from .models import *


class RallySerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Rally
        fields = '__all__'


class CrimeSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Crime
        fields = '__all__'


class PublicGatheringSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = PublicGathering
        fields = '__all__'


class NaturalCalamitiesSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = NaturalCalamities
        fields = '__all__'


class EpidemicSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Epidemic
        fields = '__all__'


