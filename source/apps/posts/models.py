from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=50, blank=True)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    comments = models.ForeignKey(
        'Comment', 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    #author = models.ForeignKey()

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
    created_at = models.DateField('Create At', auto_now_add=True)
    updated_at = models.DateTimeField('Update At', auto_now=True)


    def __str__(self):
        return f'{self.title}' #- {self.author}'



class Comment(models.Model):
    #author = models.ForeignKey()
    description = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    is_hidden = models.BooleanField(default=False)
    created_at = models.DateField('Create At', auto_now_add=True)
    updated_at = models.DateTimeField('Update At', auto_now=True)


    def __str__(self):
        return f'{self.author}', f'{self.description}'
