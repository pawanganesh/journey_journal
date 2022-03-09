from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from travel_journal.models import TravelJournal

from .serializers import TravelJournalCreateSerializer, TravelJournalSerializer, TravelJournalImageSerializer, TravelJournalUpdateSerializer


class TravelJournalCreateAPIView(CreateAPIView):
    serializer_class = TravelJournalCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TravelJournalUpdateAPIView(UpdateAPIView):
    serializer_class = TravelJournalUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TravelJournal.objects.filter(user=self.request.user)


class TravelJournalImageUpdateAPIView(UpdateAPIView):
    serializer_class = TravelJournalImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TravelJournal.objects.filter(user=self.request.user)


class TravelJournalReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = TravelJournalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TravelJournal.objects.filter(user=self.request.user)


class TravelJournalDestroyAPIView(DestroyAPIView):
    serializer_class = TravelJournalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TravelJournal.objects.filter(user=self.request.user)
