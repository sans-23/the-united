from django.contrib import admin
from .models import Question, Quiz, Report, QuizAdmin, ReportAdmin, Response, ResponseAdmin

admin.site.register(Question)
admin.site.register(Report, ReportAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Response, ResponseAdmin)