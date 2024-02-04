from django.shortcuts import render
from .models import Student_E
from django.db import connection

# Create your views here.
def student_list(request):
    posts=Student_E.objects.all()
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'orm/output.html',{'posts':posts})
    # from ORM.models import Student_E
    # >>> posts=Student_E.objects.all()
    # >>> posts
    # <QuerySet [<Student_E: Harrish>]>

def student_filter(request)

