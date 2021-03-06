# Generated by Django 4.0.5 on 2022-06-04 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_alter_task_options_alter_project_budget_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(db_index=True, max_length=300),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='issues/%Y/%m/%d')),
                ('threat_level', models.CharField(choices=[(1, 'Minor'), (2, 'Moderate'), (3, 'Critical'), (4, 'Dangerous')], max_length=50)),
                ('deadline', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comments', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='projects.comment')),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('submitted_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='projects.task')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
