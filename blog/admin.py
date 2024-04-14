from django.contrib import admin
from .models import News, Comments

# admin.site.register(models.News)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['date']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['new', 'text', 'author', 'create_date']
    search_fields = ['author']
    