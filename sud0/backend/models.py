from django.db import models



class Working_Sites(models.Model):
    class Meta:
        verbose_name = 'Working Site'
        verbose_name_plural = 'Working Sites'
    
    title = models.CharField(max_length=255, null=True, default='-')
    url = models.URLField(max_length=255, null = True, default='https://sudrf.ru/index.php?id=300&act=go_ms_search&searchtype=ms&var=true&ms_type=ms&court_subj=0', unique=True)
    adress = models.TextField(max_length=255, null = True, default='-')
    contact = models.CharField(max_length=255, null = True, default='-')
