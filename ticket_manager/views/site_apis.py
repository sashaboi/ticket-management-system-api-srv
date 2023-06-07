from ticket_manager.models import Site
from ticket_manager.serializers import SiteSerializer
from rest_framework import generics, permissions
from ticket_manager.views.auth_class import IsAuthenticated
from django.db import connection


class SiteListCreateView(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthenticated]


class SiteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthenticated]
