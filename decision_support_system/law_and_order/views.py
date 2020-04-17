from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .serializers import *


# Static pages
def index(request):
    return render(request, 'law_and_order/index.html')


def home(request):
    return render(request, 'law_and_order/home.html')


def about(request):
    return render(request, 'law_and_order/about.html')


def new_event(request):
    return render(request, 'law_and_order/new_event.html')


# Model Tables
def rally(request):
    rally_table = Rally.objects.all()
    context = {'rally_table': rally_table}
    return render(request, 'law_and_order/rally.html', context=context)


def epidemic(request):
    epidemic_table = Epidemic.objects.all()
    context = {'epidemic_table': epidemic_table}
    return render(request, 'law_and_order/epidemic.html', context=context)


def natural_calamities(request):
    natural_calamities__table = NaturalCalamities.objects.all()
    context = {'natural_calamities_table': natural_calamities__table}
    return render(request, 'law_and_order/natural_calamities.html', context=context)


def public_gathering(request):
    public_gathering_table = PublicGathering.objects.all()
    context = {'public_gathering_table': public_gathering_table}
    return render(request, 'law_and_order/public_gathering.html', context=context)


def crime(request):
    crime_table = Crime.objects.all()
    context = {'crime_table': crime_table}
    return render(request, 'law_and_order/crime.html', context=context)


# class based view for serializers
# list all rally or create a new one
class RallyDetail(APIView):

    def get_object(self, id):
        try:
            return Rally.objects.get(id=id)
        except Rally.DoesNotExist:
            raise Http404

    def get(self, request):
        rallyObject = Rally.objects.all()
        serializer = RallySerializer(rallyObject, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RallySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        to_be_deleted_id = int(request.GET['id'])
        rallyObject = self.get_object(to_be_deleted_id)
        rallyObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        to_be_deleted_id = int(request.GET['id'])
        rallyObject = self.get_object(to_be_deleted_id)
        serializer = RallySerializer(rallyObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        instance.delete()


class CrimeDetail(APIView):

    def get_object(self, id):
        try:
            return Crime.objects.get(id=id)
        except Crime.DoesNotExist:
            raise Http404

    def get(self, request):
        crimeObject = Crime.objects.all()
        serializer = CrimeSerializer(crimeObject, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CrimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        to_be_deleted_id = int(request.GET['id'])
        crimeObject = self.get_object(to_be_deleted_id)
        crimeObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        to_be_deleted_id = int(request.GET['id'])
        crimeObject = self.get_object(to_be_deleted_id)
        serializer = CrimeSerializer(crimeObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        instance.delete()


class PublicGatheringDetail(APIView):

    def get_object(self, id):
        try:
            return PublicGathering.objects.get(id=id)
        except PublicGathering.DoesNotExist:
            raise Http404

    def get(self, request):
        publicGatheringObject = PublicGathering.objects.all()
        serializer = PublicGatheringSerializer(publicGatheringObject, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicGatheringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        to_be_deleted_id = int(request.GET['id'])
        publicGatheringObject = self.get_object(to_be_deleted_id)
        publicGatheringObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        to_be_deleted_id = int(request.GET['id'])
        publicGatheringObject = self.get_object(to_be_deleted_id)
        serializer = PublicGatheringSerializer(publicGatheringObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        instance.delete()


class NaturalCalamitiesDetail(APIView):

    def get_object(self, id):
        try:
            return NaturalCalamities.objects.get(id=id)
        except NaturalCalamities.DoesNotExist:
            raise Http404

    def get(self, request):
        naturalCalamitiesObject = NaturalCalamities.objects.all()
        serializer = NaturalCalamitiesSerializer(naturalCalamitiesObject, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NaturalCalamitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        to_be_deleted_id = int(request.GET['id'])
        naturalCalamitiesObject = self.get_object(to_be_deleted_id)
        naturalCalamitiesObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        to_be_deleted_id = int(request.GET['id'])
        naturalCalamitiesObject = self.get_object(to_be_deleted_id)
        serializer = NaturalCalamitiesSerializer(naturalCalamitiesObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        instance.delete()


class EpidemicDetail(APIView):

    def get_object(self, id):
        try:
            return Epidemic.objects.get(id=id)
        except Epidemic.DoesNotExist:
            raise Http404

    def get(self, request):
        epidemicObject = Epidemic.objects.all()
        serializer = EpidemicSerializer(epidemicObject, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EpidemicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        to_be_deleted_id = int(request.GET['id'])
        epidemicObject = self.get_object(to_be_deleted_id)
        epidemicObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        to_be_deleted_id = int(request.GET['id'])
        epidemicObject = self.get_object(to_be_deleted_id)
        serializer = EpidemicSerializer(epidemicObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        instance.delete()


# model forms
def rallyform(request):
    if request.method == 'POST':
        form = RallyForm(request.POST)
        if form.is_valid():
            form.save()

    form = RallyForm()

    return render(request, 'law_and_order/new_event_rally.html', {'form': form})


def crimeform(request):
    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            form.save()

    form = CrimeForm()

    return render(request, 'law_and_order/new_event_crime.html', {'form': form})


def epidemicform(request):
    if request.method == 'POST':
        form = EpidemicForm(request.POST)
        if form.is_valid():
            form.save()

    form = EpidemicForm()

    return render(request, 'law_and_order/new_event_epidemic.html', {'form': form})


def publicgatheringform(request):
    if request.method == 'POST':
        form = PublicGatheringForm(request.POST)
        if form.is_valid():
            form.save()

    form = PublicGatheringForm()

    return render(request, 'law_and_order/new_event_public_gathering.html', {'form': form})


def naturalcalamitiesform(request):
    if request.method == 'POST':
        form = NaturalCalamitiesForm(request.POST)
        if form.is_valid():
            form.save()

    form = NaturalCalamitiesForm()

    return render(request, 'law_and_order/new_event_natural_calamities.html', {'form': form})