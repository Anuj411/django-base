from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import TourPackageSerializer
from .models import TourPackageModel


class TourPackageView(ModelViewSet):
    serializer_class = TourPackageSerializer
    queryset = TourPackageModel.objects.all()

