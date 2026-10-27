from django.shortcuts import render
from .models import Teacher, News, Book, Schedule
from django.db.models import Q

def home(request):
    latest_news = News.objects.all().order_by('-created_at')[:3]
    return render(request, 'home.html', {'latest_news': latest_news})

def news_list(request):
    news = News.objects.all().order_by('-created_at') # Сначала новые
    return render(request, 'news_list.html', {'news': news})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def book_list(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        ).distinct()
    else:
        books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books, 'query': query})


def schedule_list(request):
    classes = Schedule.objects.values_list('class_name', flat=True).distinct().order_by('class_name')

    selected_class = request.GET.get('class')
    if not selected_class and classes:
        selected_class = classes[0]

    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    rows = []

    if selected_class:
        lessons = Schedule.objects.filter(class_name=selected_class)

        max_lessons = 7

        for lesson_num in range(1, max_lessons + 1):
            row = {
                'lesson_number': lesson_num,
                'subjects': []
            }
            for day in days:
                subject = next((l.subject for l in lessons if l.day_of_week == day and l.lesson_number == lesson_num),
                               '—')
                row['subjects'].append(subject)
            rows.append(row)

    context = {
        'classes': classes,
        'selected_class': selected_class,
        'days': days,
        'rows': rows,
    }
    return render(request, 'schedule_list.html', context)