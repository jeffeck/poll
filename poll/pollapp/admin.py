from django.contrib import admin

from .models import Question, Responses, Answers  # , User

admin.site.register(Answers)
admin.site.register(Question)
admin.site.register(Responses)
# admin.site.register(User)
