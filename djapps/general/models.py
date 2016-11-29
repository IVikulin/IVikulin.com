# djapps.main.models
from django.db import models
from ckeditor.fields import RichTextField


class AboutMe(models.Model):
    title            = RichTextField(blank=True, null=True)
    email            = models.EmailField(max_length=254, blank=True, null=True)
    tel              = models.CharField(max_length=255, blank=True, null=True)
    location         = models.CharField(max_length=255, blank=True, null=True)
    github           = models.URLField(max_length=200, blank=True, null=True)
    facebook         = models.URLField(max_length=200, blank=True, null=True)
    linkedin         = models.URLField(max_length=200, blank=True, null=True)
    meta_title       = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords    = models.TextField(blank=True, null=True)
    meta_author      = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "About me"