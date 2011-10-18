from django.db import models
from tagging.fields import TagField
from django.utils.translation import ugettext_lazy as _

class Ticket(models.Model):
    
    STATUS_CHOICES = ((0, _('Open')),
                      (1, _('Closed'))
    PRIORITY_CHOICES = ((0, _('Low')),
                        (1, _('Medium')),
                        (2, _('High')))
    
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name=_('Status'))
    priority = models.IntegerField(choices=PRIORITY_CHOICES, verbose_name=_('Priority'))
    created_on = models.DateTimeField(verbose_name=_('Created on'), auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name=_('Updated on'), auto_now=True)
    tags = TagField()
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ['-status', '-priority']