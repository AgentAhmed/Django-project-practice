from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # data={

    #     'title':'Home New',

    #     'bdata':"Welcome to India | jodhpur",
    #     'clist':['PHP','JAVA','DJANGO'],
    #     'numbers':[10,20,30,40,50,60],
    #     'student_details':[
    #         {'name':'ahmed','phone':12343432},
    #         {'name':'amir','phone':4332342},
            
    #     ]
    # }
    return render(request,"index.html")  # we remove data and put it in comments for using html css js website insert
    #return render(request,"index.html",data) # we pass three parameter here
  # data is any name vraiable for dictionary, dictionary is key-value set
  # now we use 'title' key in index.html page and not 'Home New'
  # 'Home New will be shown in place of Home Page at top'
  # suppose we have a list clist then to print this we add further
  # when 'numbers':[], means number length is less then 0,then it will print No data found
    
# def homePage(request):
#      return render(request,"index.html") # we pass two parameter here

def aboutUs(request):
    return render(request,"about.html") 

def contactUs(request):
    return render(request,"contact.html")     

def gallery(request):
    return render(request,"gallery.html")   

def services(request):
    return render(request,"services.html")      


def courses(request):
    return HttpResponse('Hello, welcome to the wscubetech courses.')
def coursesDetails(request,courseid):       # courseid is a parameter for dynamic routing,this parameter will added to urls
    return HttpResponse(courseid)          # we created a function coursesDetails for showing dynamic routing.