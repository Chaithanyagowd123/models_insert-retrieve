from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def display_dept(request):
     QLOD=Dept.objects.all()
     d={'display_dept':QLOD}
     return render(request,'display_dept.html',d)



def display_emp(request):

     QLOE=Emp.objects.all()
     d={'display_emp':QLOE}
     return render(request,'display_emp.html',d)




def insert_dept(request):
     dno=input('enter deptno')
     dnames=input('enter dname')
     Loc=input('enetr loaction')

     NDO=Dept.objects.get_or_create(deptno=dno,dname=dnames,Location=Loc )[0]
     NDO.save()
     QLDO=Dept.objects.all()

     d={'display_dept':QLDO}
     return render(request,'display_dept.html',d)


def insert_emp(request):
     dno=input('enter deptno')
     en=input('enter ename')
     eid=input('enter eid')
     Salary=input('enter salary')

     EO=Dept.objects.get(deptno=dno)

     QLEO=Emp.objects.get_or_create(deptno=EO,Ename=en,Eid=eid,Sal=Salary)[0]

     QLEO.save()
     d={'display_emp':QLEO}
     return render(request,'display_emp.html',d)