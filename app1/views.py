
from django.shortcuts import HttpResponse, redirect ,render

def index(request):
    return render(request,"index.html")

def result(request):
    print("Got Post Info....................")
    # print(request.POST)
    name_from_form = request.POST['name']
    city_from_form = request.POST['city']
    languge_from_form = request.POST['language']
    message_from_form = request.POST['message']
    
    print(name_from_form)
    print(city_from_form)
    print(languge_from_form)
    print(message_from_form)
    context = {
    	"name_on_template" : name_from_form,
        "city_on_template" : city_from_form,
    	"languge_on_template" : languge_from_form,
        "message_on_template" : message_from_form,
    }
    return render(request,"result.html",context)
