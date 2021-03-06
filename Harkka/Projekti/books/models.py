from django.db import models
from django.urls import reverse

class Book(models.Model):
    nimi = models.CharField(max_length=200)
    tiedot = models.TextField(max_length=200)

    def __str__(self):
        return self.nimi

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
