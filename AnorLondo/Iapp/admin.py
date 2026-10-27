from django.contrib import admin
from .models import Teacher, News, Book, Schedule

admin.site.register(Teacher)
admin.site.register(News)
admin.site.register(Book)

# Делаем админку для расписания удобнее
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    # Показываем эти колонки в общем списке
    list_display = ('class_name', 'day_of_week', 'lesson_number', 'subject')
    # Добавляем фильтры справа
    list_filter = ('class_name', 'day_of_week')
    # Сортируем по классам и дням
    ordering = ('class_name', 'day_of_week', 'lesson_number')