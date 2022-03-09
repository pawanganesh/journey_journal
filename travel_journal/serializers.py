from rest_framework import serializers

from .models import TravelJournal


class TravelJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelJournal
        fields = '__all__'
        read_only_fields = ['id']


class TravelJournalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelJournal
        fields = ['image']


class TravelJournalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelJournal
        fields = ["title", "description", "photo", "place_name", "lat", "long"]
