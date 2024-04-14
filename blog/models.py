from django.db import models 
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField("Header", max_length=255)
    text = models.TextField("Text")
    date = models.DateTimeField("Created at", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=User)
    views = models.IntegerField("Views", default=1)
    slug = models.SlugField(verbose_name='Slug', max_length=50)
    image = models.ImageField(verbose_name='Image', upload_to='blog/%Y/%m/%d/')

    class Meta:
        # Название модели в единственном числе
        verbose_name = 'New'
        # Название модели во множественном числе
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    new = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
    # Название модели в единственном числе
        verbose_name = 'Коментарий'
    # Название модели во множественном числе
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.author.username

    