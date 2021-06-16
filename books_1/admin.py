from django.contrib import admin

from books_1.models import BookModel, CommentModel

admin.site.register(BookModel)
admin.site.register(CommentModel)
