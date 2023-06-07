from rest_framework import generics, permissions
from ticket_manager.models import Ticket
from ticket_manager.serializers import TicketSerializer


class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TicketRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]


class SiteTicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(site_id=self.kwargs['site_id'], creator=user)
