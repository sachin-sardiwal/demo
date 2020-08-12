 # todo/serializers.py

from rest_framework import serializers
from .models import Tjournal

class TjournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tjournal
        fields = ('id', 'stock', 'entryprice', 'exitprice')