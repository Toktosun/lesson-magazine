from django.test import TestCase
from django.urls import reverse


class TestPublicationListView(TestCase):

    def test_request(self):
        response = self.client.get(reverse('publication-list-url'))
        self.assertEqual(response.status_code, 200)
