from django.contrib import admin, messages
from .models import Comments, Label, News
from django.db.models import QuerySet

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # поля, которые будут отображаться
    list_display = ['name', 'activnate']
    list_display = ['name', 'activate', 'category' ]
    # поля, которые можно редактировать
    list_editable = ['activate']
    # сортировка
    ordering = ['created_at']
    list_per_page = 5
    #  поиск - для нескольких полей не получилось сделать
    search_fields = ['name']
    # действие для нескольких записей
    actions = ['publication']

    @admin.action(description="Опубликовать")
    def publication(self, request, qs:QuerySet):
        count_update = qs.update(activate=True)
        self.message_user(
            request,
            f"Было обновлено {count_update} записей",
            messages.WARNING
        )



@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 5


@admin.register(Comments)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['name_author']
    list_per_page = 5
