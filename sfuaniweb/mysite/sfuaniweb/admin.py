from django.contrib import admin
from .models import news_post,events,administration,about, gallery
# Register your models here.
admin.site.register(news_post)
admin.site.register(events)
admin.site.register(gallery)
admin.site.register(administration)

admin.site.register(about)
