from django.contrib import admin
from .models import *


#admin.site.register (UserProfile)
#admin.site.register (Article)
#admin.site.register (category)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['User', 'avatar', 'description']


admin.site.register(UserProfile, UserProfileAdmin)

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'category', 'created_at']


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover']


admin.site.register(category, CategoryAdmin)
