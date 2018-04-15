from django.contrib.auth import login, logout , authenticate
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import Login_Form , Student_Request_Form
from .models import About , Student
from django.utils import timezone
import datetime


def loginView(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mode = request.POST['mode']
        form = Login_Form(data=request.POST)

        if form.is_valid():
            print(username)
            print(password)
            print(mode)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    request.session["mode"] = mode
                    login(request, user)
                    if(request.session["mode"] == '0'):
                        return redirect('accounts:student_request_form')
                    else :
                        return redirect('accounts:allrequests')

    else:
        form = Login_Form()
    return render(request,'accounts/login.html',{'form':form})


def LogoutView(request):
    logout(request)
    try:
        del request.session['mode']
    except KeyError:
        pass

    return redirect('login')


def StudentView(request):
    if request.session["mode"] == '0':
        print(request.user)
        now = datetime.datetime.now()
        print(now.strftime("%X"))
        if request.method == "POST":
            Booking_time = request.POST['Booking_time']

            form = Student_Request_Form(request.POST)
            if ( now.strftime("%X") >= '06:00:00' and now.strftime("%X") <= '09:00:00' ) or ( now.strftime("%X") >= '16:00:00' and now.strftime("%X") <= '23:59:59' ):
                if form.is_valid():
                    print("yes")
                    info = form.save(commit=False)
                    info.username = request.user
                    info.save()
                    print("submitted")
                    form =  Student_Request_Form()
                    context ={
                        'form':form,
                        'username':request.user,
                        'mode':request.session["mode"],
                        'counterx':1,
                    }
                    return render(request , 'accounts/student_request_form.html' , context)
                else:
                     print("no")
            else :
                print("not submitted")
                context ={
                    'form':form,
                    'username':request.user,
                    'mode':request.session["mode"],
                    'counter':1,
                }
                return render(request , 'accounts/student_request_form.html' , context)
        else:
            form =  Student_Request_Form()
            context ={
                'form':form,
                'username':request.user,
                'mode':request.session["mode"],
            }
            return render(request , 'accounts/student_request_form.html' , context)
    else:
        return redirect('accounts:allrequests')


def RequestView(request , pk):
    print(request.user)
    req = Student.objects.get(pk=pk)
    if(request.session["mode"] == '1'):
        print("view")
        req.RequestViewed()
    form = Student_Request_Form(instance=req)
    print(req.pending)
    print(req.approved_comment)
    context ={
        'id':pk,
        'form':form,
        'username':request.user,
        'mode':request.session["mode"],
        'viewmodeonly':1,
        'pending':req.pending,
        'approved_comment':req.approved_comment,
    }
    return render(request , 'accounts/student_request_form.html' , context)

def RequestApprove(request , pk):
    print(request.user)
    print("approve")
    req = Student.objects.get(pk=pk)
    req.approve()
    return redirect('accounts:allrequests')

def RequestDisApprove(request , pk):
    print(request.user)
    print("disapprove")
    req = Student.objects.get(pk=pk)
    req.disapprove()
    return redirect('accounts:allrequests')


def ViewAllrequests(request):

    print(request.session["mode"])
    print(request.user)

    if request.session["mode"] == '0' :
        print("yes")
        requestlist = Student.objects.filter(username = request.user).order_by('Booking_date').order_by('Booking_time')
    else :
        print("no")
        requestlist = Student.objects.filter(pending = False).order_by('Booking_date').order_by('Booking_time')

    print(requestlist)

    context ={
        'requests_list':requestlist,
        'username':request.user,
        'mode':request.session["mode"],
    }

    return render(request, 'accounts/track_requests.html', context)
