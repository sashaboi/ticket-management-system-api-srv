from django.urls import path
from . import views
from django.urls import include, re_path

from ticket_manager.views.auth_apis import SignupView, LoginView, LogoutView
from ticket_manager.views.site_apis import SiteListCreateView, SiteRetrieveUpdateDestroyView
from ticket_manager.views.ticket_apis import TicketListCreateView, TicketRetrieveUpdateDestroyView, SiteTicketListView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sites/', SiteListCreateView.as_view(), name='site-list-create'),
    path('sites/<int:pk>/', SiteRetrieveUpdateDestroyView.as_view(),
         name='site-retrieve-update-destroy'),
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketRetrieveUpdateDestroyView.as_view(),
         name='ticket-retrieve-update-destroy'),
    path('sites/<int:site_id>/tickets/',
         SiteTicketListView.as_view(), name='site-ticket-list'),
]
