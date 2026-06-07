from django.contrib import admin
from tasks.models import Tag, Task


admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "created_at",
        "deadline",
        "is_done",
    )
    list_filter = (
        "deadline",
        "is_done",
        "tags",
        "created_at"
    )
    search_fields = ("content", )
