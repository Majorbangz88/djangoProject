from django.contrib import admin
from .models import Tweet

from .models import Comments
# Register your models here.



@admin.register(Tweet)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['text', 'last_update']
    list_per_page = 10
    search_fields = ['text']
    list_display_links = ['text']

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'comment_time', 'id']
