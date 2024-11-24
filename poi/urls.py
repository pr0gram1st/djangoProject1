from django.urls import path
from .views import PointOfInterestListCreateView, PointOfInterestDetailView

urlpatterns = [
    path('poi/', PointOfInterestListCreateView.as_view(), name='poi-list-create'),
    path('poi/<int:pk>/', PointOfInterestDetailView.as_view(), name='poi-detail'),
]
