from django.test import TestCase


# Для примера
# def calc_summa(a, b):
#     return a + b
#
#
# class TestExample(TestCase):
#
#     def test_first(self):
#         result = calc_summa(5, 15)
#         expected = 20
#         self.assertEqual(result, expected)
#
#     def test_second(self):
#         result = calc_summa(1, 3)
#         expected = 10
#         self.assertEqual(result, expected)
from apps.publications.models import PublicationCategory, Publication


class TestPublicationCategory(TestCase):

    def setUp(self) -> None:
        self.category = PublicationCategory.objects.create(title='Общая категория')
        # эта категория доступна во всех методах

    def test_create_category(self):
        cat1 = PublicationCategory.objects.create(title='Первая категория')
        self.assertEqual(cat1.title, 'Первая категория')

    def test_create_publication(self):
        publication1 = Publication.objects.create(
            title='Публикация №1', description='описанице',
            category=self.category)
        self.assertEqual(publication1.title, 'Публикация №1')
        self.assertEqual(publication1.description, 'описанице')
        self.assertEqual(publication1.category.id, self.category.id)
        self.assertIsNone(publication1.created_at)

    def test_query_all(self):
        PublicationCategory.objects.all().delete()
        new_cat = PublicationCategory.objects.create(title='Новая категория')

        category_qs = PublicationCategory.objects.all()
        self.assertEqual(len(category_qs), 1)
        self.assertEqual(category_qs[0].id, new_cat.id)

    # напишите пж тесты для методов `.filter; .count; .exclude; .first; .last;
