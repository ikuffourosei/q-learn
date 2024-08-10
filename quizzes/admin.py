from django.contrib import admin

# Register your models here.
from .models import Questions, Topics, Results, User, Choice

admin.site.register(Questions)
admin.site.register(Topics)
admin.site.register(Results)
admin.site.register(User)
admin.site.register(Choice)
