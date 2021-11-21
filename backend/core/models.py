from django.db import models


class Video(models.Model):
    title = models.CharField('título', max_length=30)
    link = models.URLField(null=True, blank=True)
    view = models.IntegerField('visualização', default=0, null=True, blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'vídeo'
        verbose_name_plural = 'vídeos'

    def __str__(self):
        return f'{self.title}'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'view': self.view,
        }
