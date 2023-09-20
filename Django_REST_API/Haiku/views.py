# api/views.py
from rest_framework import viewsets
from .models import HaikuModel
from .serializers import HaikuSerializer
from .permissions import IsOwnerOrReadOnly

class HaikuModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = HaikuModel.objects.all()
    serializer_class = HaikuSerializer
