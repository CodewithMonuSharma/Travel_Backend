from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Offer
from .serializers import OfferSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
