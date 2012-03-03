from django.db import models
from django.db.models import F

from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db.models import get_model
import logging
from django.utils.encoding import smart_str, smart_unicode
# Create your models here.
from django.utils.encoding import smart_str
from django.template.defaultfilters import slugify
from django.template.defaultfilters import  wordwrap
# Define choises
LANGUAGES_CHOISES = (
	('nl', 'nl'),
	('en', 'en'),
)
TYPE_CHOISES = (
	(1, 'Photo'),
	(2, 'Album'),
	(3, 'Movie'),
	(4, 'Note'),		
)

# Contain all projects started by adminstrator
class Projects(models.Model):
	project_id = models.AutoField(primary_key=True)
	project_name = models.CharField(_('Project name'),max_length=250)
	project_description = models.CharField(_('Project description'),max_length=1000)
	owner = OneToOneField('django.contrib.auth.User')
	date_created = models.DateTimeField(_('Date project created'))
	date_last_modified = models.DateTimeField(_('Date last modified'))
	date_last_updated = models.DateTimeField(_('Date last update run'))
	last_revision = models.IntegerField(default=0)
	last_revision_author = OneToOneField('django.contrib.auth.User')
		
		#return smart_str('%s' % (self.from_user.username))
	#@models.permalink
	def get_absolute_url(self):
		return '/project/'+ slugify(self.project_name) + '/' + self.last_revision
	
class Project_developers(models.Model):
	project_developer_id = models.AutoField(primary_key=True)
	account_id = OneToOneField('django.contrib.auth.User')
	project_id = ManyToOneField(Projects)
	date_joined = models.DateTimeField(_('Date developer joined team'))
		
