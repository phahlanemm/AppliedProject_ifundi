from django.contrib import admin
from SMS import models

# Register your models here.

#custom List View on Admin Portal
class CourseListView(admin.ModelAdmin):
    list_display = ['course_name','course_description','credits']


class StudentListView(admin.ModelAdmin):
    list_display=['first_name','last_name']


#Register the Table
admin.site.register(models.Courses, CourseListView)



admin.site.register(models.Students, StudentListView)


admin.site.register(models.Enrollments)