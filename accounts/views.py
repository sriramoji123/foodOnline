from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from vendor.forms import VendorForm
from .models import User,UserProfile
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        
        form = UserForm(request.POST)
        if form.is_valid():
            
            first_name= form.cleaned_data['first_name']
            last_name= form.cleaned_data['first_name']
            username= form.cleaned_data['first_name']
            email= form.cleaned_data['first_name']
            password= form.cleaned_data['first_name']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            messages.success(request,"your account has been registered successfully")
             
            return redirect('registration')
        else:
            print(form.errors)
            context = {
            "form": form
        } 
               
    else:
        form = UserForm()
        context = {
            "form": form,

        }

        return render(request,'accounts/registerUser.html',context)
    #return HttpResponse("This is a user registration page")
    return render(request,'accounts/registerUser.html',context)

def registerVendor(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name= form.cleaned_data['first_name']
            username= form.cleaned_data['first_name']
            email= form.cleaned_data['first_name']
            password= form.cleaned_data['first_name']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.VENDOR
            user.save() #at this point since we have written the code to create user_profile. It will be created. check in signals.py line 13
            vendor = v_form.save(commit=False)# --> this is because by now v_form only save its fields but not user_field.
            #so now we will assign vendor.user with the user
            vendor.user=user
            user_profile=UserProfile.objects.get(user=user)
            vendor.user_profile=user_profile
            vendor.save()
            messages.success(request,"Your account has been registered successfully. Please wait for the approval.")
            return redirect("registerVendor")
            
        else:
            print("invalid form")
            print(form.errors)  
    else:   
        form = UserForm()
        v_form = VendorForm()
    
    context={
        'form':form,
        "v_form":v_form,
    }
    
    return render(request, 'accounts/registerVendor.html',context)