from django.db import models
from django.urls import reverse


class Armed_university(models.Model):
    name = models.CharField(verbose_name='Имя военного вуза', max_length=120)
    location = models.CharField(verbose_name='Локация вуза', max_length=120)
    descripton = models.TextField(verbose_name='Описание')
    full_info = models.TextField(verbose_name='Полная информация')
    country = models.CharField(verbose_name='Город', max_length=120)
    main_img = models.ImageField(upload_to='photos/%Y/%m/%d')
    img_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    img_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    img_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField()

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.name
