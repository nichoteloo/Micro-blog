from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):  
    exclude = ('slug',)
    list_display = ('id', 'title', 'category', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )

admin.site.register(Blog, BlogAdmin)