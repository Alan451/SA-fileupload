from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Student
import os
# Create your views here.
@login_required
def file_upload(request):
    try:
        student = Student.objects.get(email = request.user.username)
    except:
        try:
            rollNumber = int(request.user.last_name)
            student = Student.objects.create(rollNumber = rollNumber,email = request.user.username,name = request.user.first_name)
        except:
            return redirect('roll')        
    

    if request.method == 'POST':
        files = request.FILES
        print(files)
        stud = files.get('stud',None)
        if stud is not None:
            student.antiragging_students = stud
        parent = files.get('parent',None)
        if parent is not None:
            student.antiragging_parents = parent
        cocp = files.get('cocp',None)
        if cocp is not None:
            student.code_conduct = cocp
        hostel = files.get('hostel',None)
        if hostel is not None:
            student.undertaking_hostel = hostel
        student.save()
    try:    
        antiragging_students = os.path.basename(student.antiragging_students.name)[:-4][:15]
    except:
        print("none1")
    try:
        antiragging_parents =  os.path.basename(student.antiragging_parents.name)[:-4][:15] 
    except:
        print("none2")
    try:
        code_conduct = os.path.basename(student.code_conduct.name)[:-4][:15] 
    except:    
        print("none3")
    try:
        undertaking_hostel = os.path.basename(student.undertaking_hostel.name)[:-4][:15]
    except:
        print("none4")
    print(code_conduct)
    return render(request,'file_upload.html',{'roll':student.rollNumber,'stud':antiragging_students,'parent':antiragging_parents,'cocp':code_conduct,'hostel':undertaking_hostel})

@login_required
def roll(request):
    if Student.objects.filter(email = request.user.username).exists():
        return redirect('file_upload')
    if request.method == 'POST':
        try:
            Student.objects.create(rollNumber = int(request.POST['roll']),email = request.user.username,name = request.user.first_name)
            return redirect('file_upload')
        except:
            print('kya')
    return render(request,'roll.html')