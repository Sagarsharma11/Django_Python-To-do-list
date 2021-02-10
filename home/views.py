from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from home.models import Task, Contact

idx =0

def home(request):
   

    return render(request, "index.html")


def tasks(request):

    allTasks = Task.objects.all()
    context = {'tasks': allTasks}

   # Task.objects.filter(name="Abhishek Sharma").delete()
    return render(request, "tasks.html", context)
# this function is to update the data



    


# this function delete your data

def delete_view(request, id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/tasks')

        
def delete_info(request, id):
    if request.method == 'POST':
        x = Contact.objects.get(pk=id)
        x.delete()
        return HttpResponseRedirect('/contact')
# this is my contact page



def contact(request):

    if request.method=="POST":
        name=request.POST['cname']
        email= request.POST['cemail']
        phone= request.POST['cphone']
        desc= request.POST['cdecs']

        ins= Contact(name=name, email=email, phone=phone, decs=desc)
        ins.save()
    alldata = Contact.objects.all()
    context = {'data': alldata}   
    return render(request,"contact.html", context)



def project(request):
    return render(request,"project.html")

def project2(request):

    if request.method == "POST":

        name = request.POST["name"]
        title = request.POST["title"]
        desc = request.POST['desc']

        ins = Task(name=name, title=title, decs=desc)
        ins.save()
        
    return render(request,"project2.html")
