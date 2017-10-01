from __future__ import unicode_literals

from django.db import models

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import User


# class Advertisment(models.Model):
# 	Add_title = models.CharField(max_length=200, unique=False)
# 	Add_brand = models.CharField(max_length=256,unique=False)
# 	Add_about = models.TextField()
# 	Add_views = models.IntegerField(default=0)
	

# 	def _unicode_(self):
# 		return self.Add_title

class Advertisment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	docfile = models.ImageField(upload_to='documents/%Y/%m/%d')
	Add_brand = models.CharField(max_length=256,unique=False,blank=True)
	Add_about = models.TextField(blank=True)
	Add_entry_dt = models.DateTimeField(auto_now=True)
	Add_views = models.IntegerField(default=0)


	def docfile_url(self):
		if self.docfile and hasattr(self.docfile, 'url'):
			return self.docfile.url	


	def __unicode__(self):
		return self.Add_brand


	