from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Note
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class NoteAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        self.note = Note.objects.create(
            title='Test Note',
            content='Test Note Content',
            author=self.user
        )

    def test_create_note(self):
        url = reverse('note-list')
        data = {'title': 'New Note', 'content': 'New Note Content'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)
        self.assertEqual(Note.objects.get(id=2).title, 'New Note')

    def test_update_note(self):
        url = reverse('update-note', kwargs={'pk': self.note.id})
        data = {'title': 'Updated Note'}
        response = self.client.put(url, data, format='json')

    