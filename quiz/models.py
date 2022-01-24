from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.template.defaultfilters import slugify

class Quiz(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Quiz, self).save(*args, **kwargs)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)
    question = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    marks = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)

    def __str__(self):
        return self.question

class QuestionInline(admin.TabularInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
    search_fields = ('title', 'author')
    inlines = [
        QuestionInline,
    ]

class Report(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    attempt = models.IntegerField(default=1)

    class Meta:
        unique_together = ('quiz', 'student',)
        ordering = ['-score', 'student']

    def __str__(self):
        return str(self.quiz) + ' - ' + str(self.student) + ' ' + str(self.score)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student', 'score')
    search_fields = ('quiz', 'student', 'score')

class Response(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)
    is_correct = models.BooleanField()
    attempt = models.IntegerField(default=1)

    class Meta:
        unique_together = ('quiz', 'student', 'question', 'attempt')
        ordering = ['-time']

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student', 'answer')
    search_fields = ('quiz', 'student')
