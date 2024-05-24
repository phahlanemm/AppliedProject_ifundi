import datetime
from django.shortcuts import redirect, render
from SMS import models
# Create your views here.


def students(request):
    data = {

        "StudentList" : models.Students.objects.all()

    }
    return render(request,'students.html', data)


def courselist(request):
    data = {
        "courselist": models.Courses.objects.all(),
         "StudentList" : models.Students.objects.all(),
         "ApplicationName": "School Management System -v1.0",
         "user":"Monty",

    }
    return render(request,'course.html',data)


def newstudent(request):
    if(request.method == "POST"):
        return students(request)
    else:
        return render(request,'addstudent.html')
    
# You can also separate the form handling
def displaynewStudentform(request):
    return render(request,'addstudent.html')


def saveStudent(request):
    if(request.method == "POST"):
        fname = request.POST.get('studentname')
        lname = request.POST.get('studentlastname')
        dob = request.POST.get('studentdob')
        gdr = request.POST.get('studentgender')
        edate = request.POST.get('studentenroldate')

        #Add new record to Student table

        student = models.Students(first_name = fname, last_name = lname, date_of_birth = dob, gender = gdr, enrollment_date = edate)

        models.Students.save(student)   # saves the new record to the DB using ORM

        return students(request)
    else:
        return render(request,'addstudent.html')
    

#Used to display the Form
def AddCourse(request):
    return render(request,'addcourse.html')
    
#Used to save course 
def saveCourse(request):

    #retrieving data from the request and assigning that data to variables
    coursename = request.POST.get('cname')
    coursedesc = request.POST.get('cdesc')
    coursecredit = request.POST.get('cred')
    coursecost = request.POST.get('price')

    #creating a new object/record to be saved to the database using the Class Course
    newcourse = models.Courses(
        course_name = coursename,               #setting the object attribute course_name from variable coursename
        course_description = coursedesc,
        credits = coursecredit,
        cost = coursecost
    )

    #save the record to the database
    models.Courses.save(newcourse)

#the method has to return back an http response, in our case it has called an existing method/function called courselist
    return courselist(request)



#Function to load the update page

def viewUpdateStudent(request,studentid):

    studentrec = models.Students.objects.get(student_id=studentid)

    studentrec.date_of_birth = studentrec.date_of_birth.strftime('%Y-%m-%d')
    studentrec.enrollment_date = studentrec.enrollment_date.strftime('%Y-%m-%d')

    data = {
        "student": studentrec
    }
    return render(request,'updatestudent.html',data)

# function that will display the student record to be updated
def updateStudent(request, studentno):
    data ={
        "student": models.Students.objects.get(student_id=studentno)
    }
    return render(request,'updatestudent.html', data)

#a function that will handle the form submission
def UpdateStudentRecord(request):
        fname = request.POST.get('studentname')
        lname = request.POST.get('studentlastname')
        dob = request.POST.get('studentdob')
        gdr = request.POST.get('studentgender')
        edate = request.POST.get('studentenroldate')
        studentno =  request.POST.get('studentno')
   
        student = models.Students.objects.get(student_id=studentno)

        student.first_name = request.POST.get('studentname')
        student.last_name = request.POST.get('studentlastname')
        student.date_of_birth = dob
        student.gender = gdr
        student.enrollment_date = edate
        student.save()

#        return students(request)   #it will call the method students and display the results within the same URL
        return redirect('studentlist') #Redirect will navigate to URL named 'studentlist'


def home(request):
    return render(request,'index.html')