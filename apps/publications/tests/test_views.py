import io

from django.core.files.images import ImageFile
from django.test import TestCase
from django.urls import reverse

from apps.publications.models import Publication


class TestPublicationListView(TestCase):

    def test_publication_list(self):
        url = reverse('publication-list-url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_publication_detail_view(self):
        temporary_image = ImageFile(io.BytesIO(b'some-file'), name='foo.jpg')
        pub = Publication.objects.create(title='some', description='desc',
                                         poster=temporary_image)
        url = reverse('publication-detail-url', kwargs={'pub_pk': pub.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
