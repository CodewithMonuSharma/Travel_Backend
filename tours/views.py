from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, BasePermission, SAFE_METHODS
from .models import TourPackage
from .serializers import TourPackageListSerializer, TourPackageDetailSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class TourPackageListCreateView(generics.ListCreateAPIView):
    queryset = TourPackage.objects.filter(is_active=True)
    permission_classes = [IsAdminOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TourPackageDetailSerializer
        return TourPackageListSerializer

class TourPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageDetailSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'
