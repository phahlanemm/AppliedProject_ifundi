from django.db import models

# Create your models here.

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(blank=True, null=True)
    credits = models.IntegerField()
    cost = models.DecimalField(max_digits=7, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'courses'


class Enrollments(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Students', models.DO_NOTHING)
    course = models.ForeignKey(Courses, models.DO_NOTHING)
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollments'


class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    enrollment_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'students'
