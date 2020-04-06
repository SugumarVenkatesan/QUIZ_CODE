from django.contrib import admin

# Register your models here.
import nested_admin
from .models import Quiz, Question, Answer, Response, QuizTakers
from nested_admin import nested

class AnswerInline(nested_admin.nested.NestedTabularInline):
    model = Answer
    extra = 1

class QuestionInline(nested_admin.nested.NestedTabularInline):
    model = Question
    inlines = [AnswerInline,]
    extra = 1

class QuizAdmin(nested_admin.nested.NestedModelAdmin):
    inlines = [QuestionInline]

class ResponseInline(admin.TabularInline):
    model = Response
    
class QuizTakersAdmin(admin.ModelAdmin):
    inlines = [ResponseInline,]
    

admin.site.register(Quiz,QuizAdmin)
admin.site.register(QuizTakers, QuizTakersAdmin)
admin.site.register(Response)

