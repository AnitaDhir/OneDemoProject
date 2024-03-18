from django.shortcuts import render, HttpResponseRedirect ,redirect
from .forms import StudentRegistration
from .models import User


# from django.core.mail import send_mail
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from .forms import StudentRegistration
# from .models import User



# Create your views here.
# this will add and show items


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            gd = fm.cleaned_data['gender']
            dob = fm.cleaned_data['date_of_birth']
            pn = fm.cleaned_data['parent_name']
            reg = User(name=nm,email=em,gender=gd,date_of_birth=dob,parent_name=pn)
            reg.save()
            
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request,'enroll/addandshow.html', {'form':fm, 'stu':stud})




from django.shortcuts import render, redirect
from .forms import StudentRegistration  # Assuming StudentRegistration is your form

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('addandshow')  # Redirect to the page where you display student information
    else:  
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    
    return render(request, 'enroll/updatestudent.html', {'form': fm})



# This function will delete 
def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        
        return HttpResponseRedirect('/')

# def send_registration_email(name, email):
#     subject = 'Registration Confirmation'
#     message = f'Dear {name},\n\nThank you for registering with us.'
#     from_email = 'no-reply@itsm-indeftts.com'
#     recipient_list = [email]
#     send_mail(subject, message, from_email, recipient_list)

