  # tjournal/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TjournalSerializer      # add this
from .models import Tjournal                     # add this

class TjournalView(viewsets.ModelViewSet):       # add this
    serializer_class = TjournalSerializer          # add this
    queryset = Tjournal.objects.all()   