def approve_comment(modeladmin, request, queryset):
    queryset.update(aproved=True)


def disapprove_comment(modeladmin, request, queryset):
    queryset.update(aproved=False)

disapprove_comment.short_description="Reprovar comentário"
approve_comment.short_description="Aprovar comentário"