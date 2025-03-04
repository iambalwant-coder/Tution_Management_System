from django.shortcuts import render,redirect
from .models import Student_models
from .forms import StudentForm


# Create your views here.



def home_views(request):
    students = Student_models.objects.all()
    return render(request, 'home.html', {'students': students})

def add1_views(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm=StudentForm()
    return render(request,'add1.html',{'form':fm})

def add2_views(request):
    if request.method=='POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        student_age = request.POST.get('student_age')
        student_gender = request.POST.get('student_gender')
        total_fee = request.POST.get('total_fee')
        paid_fee = request.POST.get('paid_fee')

        obj = Student_models()
        obj.student_id = student_id
        obj.student_name = student_name
        obj.student_age = student_age
        obj.student_gender = student_gender
        obj.total_fee = total_fee
        obj.paid_fee = paid_fee
        obj.save()
        return redirect('/')
    else:
        return render(request, 'add2.html')

def delete1_views(request):
    data = Student_models.objects.all()
    if request.method=='POST':
        id = request.POST['id']
        detete = Student_models.objects.get(student_id=id)
        print('-------: Deleted :-------')
        print("Roll Num : ",detete.student_id)
        print("Roll Name : ",detete.student_name)
        print("Roll Age : ",detete.student_age)
        print("Roll Gender : ",detete.student_gender)
        print("Total Fee : ",detete.total_fee)
        print("Paid Fee : ",detete.paid_fee)
        print('-------------------------')
        detete.delete()
        return redirect('delete1')
    return render(request,'delete1.html',{'students':data})

    
def delete2_views(request,id):
    delete = Student_models.objects.get(pk=id)
    delete.delete()
    return redirect('/')

def edit_views(request,id):
    obj = Student_models.objects.get(pk=id)
    return render(request,'edit.html',{'students':obj})