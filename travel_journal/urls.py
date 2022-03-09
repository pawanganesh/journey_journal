from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import TravelJournalCreateAPIView, TravelJournalUpdateAPIView, TravelJournalReadOnlyViewSet, TravelJournalDestroyAPIView, TravelJournalImageUpdateAPIView


router = DefaultRouter()

router.register(r'', TravelJournalReadOnlyViewSet, basename='travel_journal_read_only')


app_name = 'travel_journal'
urlpatterns = [
    path('add', TravelJournalCreateAPIView.as_view(), name='create'),
    path('<int:pk>', TravelJournalUpdateAPIView.as_view(), name='update'),
    path('photo/<int:pk>', TravelJournalImageUpdateAPIView.as_view(), name='image-update'),
    path('delete/<int:pk>', TravelJournalDestroyAPIView.as_view(), name='destroy'),
] + router.urls
