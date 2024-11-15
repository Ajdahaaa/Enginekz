from django.db import models
from pytils.translit import slugify
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField("Название категории",max_length=255)
    slug = models.SlugField(unique=True,editable=False,blank=True)
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
class Guide(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание гайда")
    image = models.CharField("URL-фото",max_length=500)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Гайд"
        verbose_name_plural = "Гайды"

    def __str__(self):
        return self.title