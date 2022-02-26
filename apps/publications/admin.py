from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail

from apps.publications.models import Publication, PublicationCategory


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

    def save_model(self, request, obj, form, change):
        if not change:
            print(f'СОЗДАНИЕ ПУБЛИКАЦИИ С АДМИНКИ')
            try:
                send_mail(
                    subject='Вам пришло новое сообщение.',
                    message='Создалась новая публикация. УРА',
                    from_email=settings.EMAIL_HOST_USER,  # отправитель
                    recipient_list=['toktosunalphadev@gmail.com'],  # получатели
                )
            except Exception as exc:
                print(exc)
            # альтернативный способ
            # send_mail(
            #     subject='Вам пришло новое сообщение.',
            #     message='Создалась новая публикация. УРА',
            #     from_email=settings.EMAIL_HOST_USER,  # отправитель
            #     recipient_list=['toktosunalphadev@gmail.com'],  # получатели
            #     fail_silently=True,  благодаря этому параметру, программа не упадёт в случае ошибки
            # )
        return super(PublicationAdmin, self).save_model(request, obj, form, change)


@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    pass
