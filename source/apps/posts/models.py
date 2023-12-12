from django.db import models
from datetime import timezone

class Post(models.Model):
    author = models.ForeignKey()
    title = models.CharField(max_length=25, verbose_name='Título do post')
    description = models.CharField(max_length=255, verbose_name='Descrição do post')
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE)
    language = models.CharField(max_length=25, verbose_name='Linguagem utilizada no post')
    knowledge_level = models.IntegerField(verbose_name='Nível de conhecimento')

    send_at = models.DateTimeField(auto_now_add=True, verbose_name='Data e horário de envio')
    create_at = models.DateField('Create At', default=timezone.now)
    is_hidden = models.BooleanField(default=False)
    updated_at = models.DateTimeField('Update At', default=timezone.now)

    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f'{self.title}',  f'{self.author}'


class Comment(models.Model):
    author = models.ForeignKey()
    description = models.CharField(
        max_length=255, verbose_name='Descrição do comentário')
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}', f'{self.description}'
