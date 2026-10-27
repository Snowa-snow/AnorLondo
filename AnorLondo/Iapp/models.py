from django.db import models

class Teacher(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    subject = models.CharField("Предмет", max_length=100)
    bio = models.TextField("О учителе", blank=True)
    photo = models.ImageField("Фото", upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.subject})"

class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст новости")
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField("Название книги", max_length=200)
    author = models.CharField("Автор", max_length=150)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return f"{self.title} — {self.author}"

class Schedule(models.Model):
    day_of_week = models.CharField("День недели", max_length=20)
    lesson_number = models.IntegerField("Номер урока")
    subject = models.CharField("Предмет", max_length=100)
    class_name = models.CharField("Класс", max_length=20, default="5А")

    def __str__(self):
        return f"{self.day_of_week} | Урок {self.lesson_number}: {self.subject} ({self.class_name})"