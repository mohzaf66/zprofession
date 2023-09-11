from django.contrib import admin
from .models import Contact,Post,Comment,Website
# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Website)