from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


status = (
	('C', 'Completed'),
	('A', 'Active'),
	('P', 'Paused'),
	('S', 'Stuck'),
	)

priority = (
	('L', 'Low-priority'),
	('I', 'Important'),
	('N', 'Not important'),
	('U', 'Urgent'),
	('X', 'Xtra Important'),
	)

due = (
	('C', 'Completed'),
	('O', 'Overdue'),
	('D', 'Due'),
	('E', 'Eliminated'),
	)

danger_level = (
	('1', 'Minor'),
	('2', 'Moderate'),
	('3', 'Critical'),
	('4', 'Dangerous'),
	)

class Comment(models.Model):
	user = models.ManyToManyField(User)
	comment = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Project(models.Model):
	company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)

	title = models.CharField(max_length=300, db_index=True)
	slug = models.SlugField(max_length=300, db_index=True, unique=True)
	user = models.ManyToManyField(User)
	
	description = models.TextField(blank=True)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	deadline = models.DateField()

	status = models.CharField(max_length=50, choices=status)
	budget = models.DecimalField(max_digits=12, decimal_places=2)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('projects:project_detail', args=[self.id])


class Task(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	title = models.CharField(max_length=300, db_index=True)
	slug = models.SlugField(max_length=300)
	user = models.ManyToManyField(User)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	description = models.TextField()
	priority = models.CharField(max_length=50, choices=priority)
	status = models.CharField(max_length=50, choices=due)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('projects:task_detail', args=[self.project.id, self.id])


class Issue(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	description = models.TextField()
	image = models.ImageField(upload_to="issues/%Y/%m/%d", blank=True)

	threat_level = models.CharField(max_length=50, choices=danger_level)

	deadline = models.DateTimeField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	submitted_by = models.ManyToManyField(User, default='')

	project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True)
	task = models.ForeignKey(Task, on_delete=models.PROTECT, blank=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('projects:issue_detail', args=[self.id])
