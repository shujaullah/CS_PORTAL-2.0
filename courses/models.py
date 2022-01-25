from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Semesters(models.Model):
    semester_abbrev = models.CharField(max_length=8, primary_key=True)
    semester_longname = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Semesters'
        verbose_name_plural = 'Semesters'

    def __unicode__(self):
        return self.semester_longname

class Courses(models.Model):
    # we can say blank=True if the field is not required.
    user = models.ManyToManyField(User, blank=True)
    course_number = models.CharField(max_length=8)
    course_section = models.CharField(max_length=8)
    course_name = models.CharField(max_length=60)
    course_instructor = models.CharField(max_length=60)
    course_description = models.TextField(blank=True)
    course_semester = models.ForeignKey(Semesters, on_delete=models.CASCADE)
    course_active = models.BooleanField(default=False)
    course_notes = models.CharField(max_length=255, default="", blank=True)

    class Meta:
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course_name



