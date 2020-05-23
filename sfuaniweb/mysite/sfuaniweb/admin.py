from django.contrib import admin
from .models import news_post,events,administration,about
# Register your models here.
admin.site.register(news_post)
admin.site.register(events)

admin.site.register(administration)

admin.site.register(about)
