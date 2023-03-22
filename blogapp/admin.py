from django.contrib import admin
from .models import BlogPost

admin.site.site_header = 'Administration du site'
admin.site.site_title = 'CLEASON DASHBOARD'
# admin.site.site_url = 'ahjv-togo'

@admin.register(BlogPost)
class AdminBlogPost(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_on', 'published', 'last_updated')
    search_fields = ('title', 'content')
    list_filter = ('author', 'title')
