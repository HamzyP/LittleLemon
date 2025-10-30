from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def menu(request):
    menu_items = Menu.objects.all()
    context = {
        'menu' : menu_items
    }
    return render(request, 'menu.html', context)

class MenuItemsView(generics.ListCreateAPIView):
    # does POST and GET method calls
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    # Does the GET PUT DELETE method calls
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]