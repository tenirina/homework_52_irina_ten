from django.contrib import admin


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'status', 'completion_data')
    list_filter = ('id', 'text', 'status', 'completion_data')
    search_fields = ('text', 'status', 'completion_data')
    fields = ('id', 'text', 'status', 'completion_data')
