from django.db import models

from django.contrib.auth import get_user_model


USER = get_user_model()


class TravelJournal(models.Model):
    """
    A travel journal.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')
    place_name = models.CharField(max_length=255, null=True)
    lat = models.DecimalField(max_digits=30, decimal_places=10)
    long = models.DecimalField(max_digits=30, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
