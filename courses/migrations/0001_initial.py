# Generated by Django 4.0 on 2022-01-25 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('semester_abbrev', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('semester_longname', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Semesters',
                'verbose_name_plural': 'Semesters',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=8)),
                ('course_section', models.CharField(max_length=8)),
                ('course_name', models.CharField(max_length=60)),
                ('course_instructor', models.CharField(max_length=60)),
                ('course_description', models.TextField(blank=True)),
                ('course_active', models.BooleanField(default=False)),
                ('course_notes', models.CharField(blank=True, default='', max_length=255)),
                ('course_semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.semesters')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Courses',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
