from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class news_post(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class events(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class administration(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class gallery(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")
    hotel_Main_Img = models.ImageField(upload_to='img/index-gallery/')
    datetime = models.DateField()


class about(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()
