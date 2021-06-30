from django.shortcuts import render, HttpResponse
from .utils import *
from .models import *
import pandas
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def Generate_Student_Data(request):
    try:
         student_data()
        return HttpResponse('Student Fake Data Created')

    except Exception as e:
        print(e) 
    return HttpResponse('Some Thing Wroung')


    
def covertdata(request):

    try:
        data=[]
        stu_obj = list(Student.objects.all())
        for obj in stu_obj:
            mylist = [obj.student_name, obj.student_age, obj.student_email, obj.student_phoneno,obj.student_address]
            data.append(mylist)
        data = pandas.DataFrame(data)
        print(data)
        data.to_excel("excel/output.xlsx")
        return HttpResponse('converted')
    except Exception as e:
        print(e)
    return HttpResponse('something wroung')


def sendmail(request):
    try:
        email_obj = Emails.objects.all()
        for i in email_obj:
            sub = "Student Excel file"
            body = f"Hay,{i.Name} THis is our student list grab it."
            msg = EmailMessage(sub, body, settings.EMAIL_HOST_USER,  [i.Email])
            msg.content_subtype = "html"  
            msg.attach_file("excel/output.xlsx")
            msg.send()
            return HttpResponse('email sent')

    except Exception as e:
        print(e)   
    return HttpResponse('something wroung')     
