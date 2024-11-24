from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PointOfInterest
from .serializers import PointOfInterestSerializer

class PointOfInterestListCreateView(generics.ListCreateAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        queryset = PointOfInterest.objects.all()
        if category:
            queryset = queryset.filter(category__iexact=category)
        return queryset


class PointOfInterestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
