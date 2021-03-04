from django.contrib import admin
from .models import Student
# Register your models here.
import csv
from django.http import HttpResponse
from django.conf import settings
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3
class StudentAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ('rollNumber','name', 'email',  'antiragging_students' ,'antiragging_parents','code_conduct', 'undertaking_hostel')
    def download_csv(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(['rollNumber','name', 'email',  'antiragging_students' ,'antiragging_parents','code_conduct', 'undertaking_hostel'])

        for s in queryset:
            try:
                stud = 'https://swc.iitg.ac.in'+s.antiragging_students.url
            except:
                stud = 'N/A'
            try:
                parent = 'https://swc.iitg.ac.in'+s.antiragging_parents.url
            except:
               parent = 'N/A'
            try:
                cocp = 'https://swc.iitg.ac.in'+s.code_conduct.url
            except:
                cocp = 'N/A'

            try:
                hostel = 'https://swc.iitg.ac.in'+s.undertaking_hostel.url
            except:
                hostel = 'N/A'         
            
            writer.writerow([s.rollNumber,s.name, s.email, stud ,parent,cocp, hostel])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=student-details.csv'
        return response
    download_csv.short_description = "Download CSV file for selected stats."

admin.site.register(Student,StudentAdmin)