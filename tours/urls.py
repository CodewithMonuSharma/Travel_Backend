from django.urls import path
from .views import TourPackageListCreateView, TourPackageDetailView

urlpatterns = [
    path('', TourPackageListCreateView.as_view(), name='tour_package_list'),
    path('<slug:slug>/', TourPackageDetailView.as_view(), name='tour_package_detail'),
]
