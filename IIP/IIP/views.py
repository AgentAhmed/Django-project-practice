from dataclasses import dataclass
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from .forms import usersForm
from service.models import Service
from news.models import News
from autoslug import AutoSlugField
from django.core.paginator import Paginator   
from contactenquiry.models import contactEnquiry  


# def homePage(request):
#     data = {
#         'title':'WsCubeTech',
#         'bdata':'Welcome to Wscubetech',
#         'clist':['PHP','Java','Django'],
#         'numb':[10,20,30,40,50 ],
#         'roll':[],
#         'student_details':[
#             {'name':'pradeep','phone':57463456357,'country':'India'},
#             {'name':'testing','phone':35467868899,'country':'America'},
#             {'name':'Ahmed','phone':1234567866,'country':'Rome'},
#         ]
#     }
#     return render(request,"index.html",data)   # for render we import library shortucts , two parameters required for render

# def homePage(request):
#     return render(request,"index1.html")   # using it for website template we paste in template folder and given name index1.html to avoid overlapping with index.html

def homePage(request):          # we are doing this to check marquee tag admin dashboard models etc
    newsData=News.objects.all()

    data={

        'newsData':newsData
    }


    return render(request,"index1.html",data)

def newsDetails(request,newsid):

    newsDetails=News.objects.get(id=newsid)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsdetails.html",data)


def aboutUs(request):
    return render(request,"about.html")

def submitform(request):

    finalans = 0
    fn=usersForm()

    data={'form':fn}

    try:
     if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
           
            finalans=n1+n2
            
            data= {
                'form':fn,
                'n1':n1,
                'n2':n2,
                'output':finalans
             }  
            #url="/about-us/?output={}".format(finalans) 

            #return HttpResponseRedirect(url)
            return HttpResponse(finalans)  # this will print the result on submit page and not redirect to other page
    except:
            pass     
      

def contactUs(request):
     
    return render(request,"contact.html")

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('Name:')
        email=request.POST.get('Email:')
        subject=request.POST.get('Subject:')
        message=request.POST.get('Message:')

        en=contactEnquiry(name=name,email=email,subject=subject,message=message)
        en.save()
        
    return render(request,"contact.html")    

    

def gallery(request):
    return render(request,"gallery.html") 

def service(request):
    # _icontains
    #serviceData=Service.objects.all().order_by('service_title')  # this is ascending order_by alphabetically
   # serviceData=Service.objects.all().order_by('-service_title')  # this is descending order_by alphabetically
    # serviceData=Service.objects.all().order_by('service_title')[2:5] # we are putting here limit
    # for a in serviceData:
    #     print(a.service_title)
    # print(service)         
    # serviceData=Service.objects.all().order_by('service_title')
    serviceData=Service.objects.all()

    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            serviceData=Service.objects.filter(service_title=st)
    data={

        'serviceData':serviceData
    }

    return render(request,"services.html",data)    
 
def userForm(request):
    finalans = 0
    fn=usersForm()

    data={'form':fn}
    
    try:
            #n1=int(request.GET['num1'])
            #n2=int(request.GET['num2'])
            
            # if request.method=="POST":    
            # n1=request.POST['num1']
            # n2=request.POST['num2'] 
            #or
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
           
            finalans=n1+n2
            
            data= {
                'form':fn,
                'output':finalans
             }  
            url="/about-us/?output={}".format(finalans) 

            return HttpResponseRedirect(url)
    except:
            pass     
    
    return render(request,"userForm.html",data)  

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))  # eval use for number and float value
            opr=request.POST.get('opr')
            
           

            if opr=="+":
                c= n1 + n2;

            elif opr=="-":
                c= n1 - n2;

            elif opr=="/":
                c= n1 / n2;

            elif opr=="*":
                c= n1 * n2;            

    except:
        c="Invalid operation"    
        print(c) 
    
    return render(request,"calculator.html",{'c':c})  
 
def evenodd(request):
       
        c='' 
        if request.method=="POST":
             
            if request.POST.get('num1')=="":
                
                return render(request,"evenodd.html",{'error':True})  

            n=eval(request.POST.get('num1'))
            if n%2==0:
                c="Even Number"
            else:
                c="Odd Number"        
            
        return render(request,"evenodd.html",{'c':c})    
    

        
def marks(request):

    if request.method=="POST":
        s1=eval(request.POST.get('subject1')) 
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))

        t=s1+s2+s3+s4+s5
        p=t*100/500;
        if p>=60:
            d="First Div"
        elif p>=48:
            d="Second Div"
        elif p>=35:
            d="Third Div"
        else :
            d="Fail"                  
        
        data={
            'total':t,
            'per':p,
            'div':d
        }
 
    return render(request,"marks.html",data) 
    return render(request,"marks.html")        
def course(request):
    return HttpResponse("Advanced Python course")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

  