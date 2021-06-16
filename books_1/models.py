from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(max_length=255)
    is_booked = models.ForeignKey(UserModel,
                                  on_delete=models.CASCADE,
                                  related_name='booked',
                                  null=True,
                                  blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_comment')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='book_comment')
    text = models.TextField()

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
