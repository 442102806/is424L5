from django.shortcuts import render

people = []

class Person:

    def __init__(self, username, password):
        self.username = username
        self.password = password   
    
def home(request):
    return render(request, "home.html", {'people': people})   
           
def add(request):    
     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         person = Person(username=username, password=password)
         people.append(person)
     return render(request,'index.html')

