"""magazine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.publications.views import PublicationListView, PublicationDetailView, \
    accept_show_user_mail_form_view
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('publication-list/', PublicationListView.as_view(),
         name='publication-list-url'),
    path('publication-list/<int:pub_pk>/', PublicationDetailView.as_view(),
         name='publication-detail-url'),
    path('user-email/', accept_show_user_mail_form_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
