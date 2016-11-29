# djapps.portfolio.models
from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField


class Skill(models.Model):
    SKILL_GROUPS = (
        ('B', 'Back-end'),
        ('F', 'Front-end'),
    )

    group       = models.CharField(max_length=1, choices=SKILL_GROUPS, 
                                   default=SKILL_GROUPS[0][0])
    name        = models.CharField(max_length=255)
    order       = models.PositiveIntegerField(default=0, blank=False, 
                                              null=False)

    def __str__(self):
        return '%s - %s' % (self.get_group_display(), self.name)

    class Meta:
        ordering = ('order',)


class Work(models.Model):
    name        = models.CharField(max_length=255)
    img         = ImageField(upload_to='img/works', blank=True, null=True)
    url         = models.URLField(max_length=200, blank=True, null=True)
    order       = models.PositiveIntegerField(default=0, blank=False, 
                                              null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order',)