from django.db import models
from django.urls import reverse


class Company(models.Model):
	name = models.CharField(max_length=300, db_index=True)
	slug = models.SlugField(max_length=300, db_index=True, unique=True)

	email = models.EmailField(blank=True, default='')
	website = models.URLField(blank=True, default='')
	location = models.CharField(max_length=150, blank=True, default='')
	
	about = models.TextField(blank=True, default='')

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Company'
		verbose_name_plural = 'Companies'
		ordering = ('name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("companies:company_detail", args=[self.id])
