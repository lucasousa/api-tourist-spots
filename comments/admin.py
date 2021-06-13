from django.contrib import admin
from .models import Comment
from .actions import *


class CommentAdmin(admin.ModelAdmin):
    list_display=('user', 'date', 'aproved')
    actions=[approve_comment, disapprove_comment]

admin.site.register(Comment,CommentAdmin)
