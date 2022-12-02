from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import AdminsExtraSerializer, AreasSerializer, ChamadosSerializer
from .models import AdminsExtra, Areas, Chamados


class AdminsExtraViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    queryset = AdminsExtra.objects.all()
    serializer_class = AdminsExtraSerializer
    
class AreasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer
    
class ChamadosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    queryset = Chamados.objects.all()
    serializer_class = ChamadosSerializer