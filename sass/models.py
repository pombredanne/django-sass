from django.db import models
from django.conf import settings

from sass.utils import SassUtils


class SassModel(models.Model):
    name = models.CharField(max_length=60, primary_key=True, help_text='Name of the Sass conversion.')
    sass_path = models.CharField(max_length=255, help_text='Path submitted for the Sass file.')
    css_path = models.CharField(max_length=255, help_text='Path to the generated CSS file.')
    digest = models.CharField(max_length=32, help_text='Unique digest used to identify source files.')
    
    def __unicode__(self):
        return self.name
        
    def relative_css_path(self):
        return self.css_path.split(settings.MEDIA_ROOT)[1].lstrip('/')
        
    def css_media_path(self):
        return SassUtils.get_media_url(path=self.relative_css_path())