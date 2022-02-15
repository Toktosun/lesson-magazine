from django.http import Http404
from django.shortcuts import render
from django.views import generic

from apps.publications.models import Publication, PublicationCategory


# localhost:8000/publications/
# localhost:8000/publications/?search_word=ноутбук
class PublicationListView(generic.ListView):
    """Показ всех публикаций"""
    template_name = 'index.html'
    context_object_name = 'publication_list'

    def get_queryset(self):
        query_params = self.request.GET  # тип словарь
        search_word = query_params.get('search_word')
        if search_word:
            publication_qs = Publication.objects.filter(title__contains=search_word)
        else:
            publication_qs = Publication.objects.all()
        return publication_qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PublicationListView, self).get_context_data(**kwargs)
        context['category_list'] = PublicationCategory.objects.all()
        return context

# старый способ
# class PublicationListView(generic.TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(PublicationListView, self).get_context_data(**kwargs)
#         context['publication_list'] = Publication.objects.all()
#         return context


class PublicationDetailView(generic.DetailView):
    template_name = 'single.html'
    context_object_name = 'publication'
    model = Publication
    slug_field = 'id'
    slug_url_kwarg = 'pub_pk'

# старый способ
# class PublicationDetailView(generic.TemplateView):
#     template_name = 'single.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(PublicationDetailView, self).get_context_data(**kwargs)
#         publication_pk = kwargs['pub_pk']
#         try:
#             context['publication'] = Publication.objects.get(id=publication_pk)
#         except Publication.DoesNotExist:
#             raise Http404
#         return context
