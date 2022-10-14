from rest_framework import generics
from inv.models import Items
from .serializers import ItemSerializer

class ApiItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()

class ApiItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()