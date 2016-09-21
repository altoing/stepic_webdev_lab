from django.contrib import admin

# Register your models here.
from .models import Users, Question, Answer

admin.site.register(Users)
admin.site.register(Question)
admin.site.register(Answer)