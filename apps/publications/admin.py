from django.contrib import admin

from apps.publications.models import Publication, PublicationCategory


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    pass
