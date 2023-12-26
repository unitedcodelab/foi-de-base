from django.db import models
from people.models import Student


class Post(models.Model):
    slug = models.SlugField(max_length=50, blank=True)
    title = models.CharField(max_length=25)
    content = models.CharField(max_length=255)
    comments = models.ForeignKey(
        'Comment', 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        Student,
        related_name='posts', 
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    language = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )
    knowledge_level = models.IntegerField(
        blank=True,
        null=True,
    )

    is_hidden = models.BooleanField(default=False)
    created_at = models.DateField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)


    def __str__(self):
        return f'{self.title}, slug: {self.slug}'



class Comment(models.Model):
    author = models.ForeignKey(
        Student,
        related_name='comments', 
        on_delete=models.PROTECT,
        default=None,
    )
    description = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        default=None,
    )

    is_hidden = models.BooleanField(default=False)
    created_at = models.DateField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)


    def __str__(self):
        return f'{self.description}'
