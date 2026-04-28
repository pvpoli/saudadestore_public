from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Title(models.Model):
    title_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title_text


class Photos(models.Model):
    #the name of the image file
    photos_name = models.CharField(max_length=200, default="", blank=True)
    photos_item = models.ImageField(max_length=2000, default="fachada.jpg", upload_to='media')

    def image_tag(self):
        if self.photos_item:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photos_item.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.photos_name

class HomepagePhotos(models.Model):
    #the name of the image file
    photos_name = models.CharField(max_length=200, default="", blank=True)
    photos_item = models.ImageField(max_length=2000, default="", upload_to='media')

    def image_tag(self):
        if self.photos_item:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photos_item.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.photos_name

class HomepagePhotosMobile(models.Model):
    #the name of the image file
    photos_name = models.CharField(max_length=200, default="", blank=True)
    photos_item = models.ImageField(max_length=2000, default="", upload_to='media')

    def image_tag(self):
        if self.photos_item:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photos_item.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.photos_name

class QuemSomos(models.Model):
    text_quemsomos = models.TextField()
    photos_item = models.ImageField(max_length=2000, default="", upload_to='media')
    
    def image_tag(self):
        if self.photos_item:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photos_item.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
    
    def __str__(self):
        return self.text_quemsomos

class AlforrecaTexto(models.Model):
    text_alforreca = models.TextField()
    photos_item = models.ImageField(max_length=2000, default="", upload_to='media')

    def image_tag(self):
        if self.photos_item:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photos_item.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
        
    def __str__(self):
        return self.text_alforreca

class AlforrecaImagens(models.Model):
    #the name of the image file
    photos_name = models.CharField(max_length=200, default="", blank=True)
    photos_item = models.ImageField(max_length=2000, default="", upload_to='media')

    def image_tag(self):
        if self.photos_item:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photos_item.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.photos_name

class ComoChegar(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    
    def __str__(self):
        return self.titulo