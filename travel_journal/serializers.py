from rest_framework import serializers

from .models import TravelJournal


class TravelJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelJournal
        fields = ["title", "description", "place_name", "lat", "long"]


class TravelJournalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelJournal
        fields = ['photo']


class TravelJournalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelJournal
        fields = ["title", "description", "photo", "place_name", "lat", "long"]
