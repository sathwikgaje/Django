# from email import message
from django.shortcuts import render , redirect
from .models import StatesTb,JobsDetailsTb,JobSubCategoriesTb,JobCategoriesTb,CompanyDetailsTb,DetailsTb,SubDetailsTb
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

values = {
    'pk_test' : " ",
    'pk_data' : " ",
    'pk_value' : " "
}
def category(request,pk_test):
    categories = JobCategoriesTb.objects.all()
    values['pk_test'] = pk_test
    data = {
            'categories' : categories,
            'pk_test' : pk_test,
        }
    return render(request,'temp/category.html',data)

def subcategory(request,pk_test,pk_data):
    subcategories = DetailsTb.objects.filter(category = pk_data)
    values['pk_data'] = pk_data
    data={
        'subcategories' : subcategories,
        'pk_test': pk_test,
        'pk_data': pk_data
    }
    return render(request,'temp/subcategory.html',data)

def Jobs(request,pk_data,pk_test,pk_value):
    jobs = JobsDetailsTb.objects.filter(category = pk_data,sub_category = pk_value,location = pk_test)
    values['pk_value'] = pk_value
    data={
        'jobs':jobs
    }
    return render(request,'temp/jobs.html',data)


def states(request):
    states = StatesTb.objects.all()
    data = {
        'states' : states
    }
    return render(request,'temp/states.html',data)


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Created Successfully')
            return redirect('Home-Page')
    else:
        form = CreateUserForm()
    context ={ 'form':form }
    return render(request,'temp/register.html',context)

def search_states(request):
    if request.method == "POST":
        searched = request.POST['searched']
        states = StatesTb.objects.filter(location__contains = searched)
        return render(request, 'temp/search_states.html',{'searched':searched , 'states':states})

def search_category(request):
    if request.method == "POST":
        searched = request.POST['searched']
        categories = JobCategoriesTb.objects.filter(category__contains = searched)
        data = {
            'categories' : categories,
            'searched' : searched,
            'pk_test' : values['pk_test']
        }
        return render(request,'temp/search_category.html',data)

def search_sub_category(request):
    if request.method == "POST":
        searched = request.POST['searched']
        subcategories = DetailsTb.objects.filter(category = values['pk_data']).filter(sub_category__contains = searched)
        data={
            'subcategories' : subcategories,
            'pk_test':values['pk_test'],
            'pk_data':values['pk_data'],
            'searched' : searched
            }
        return render(request,'temp/search_sub_category.html',data)

def search_jobs(request):
    if request.method == "POST":
        searched = request.POST['searched']
        jobs = JobsDetailsTb.objects.filter(category = values['pk_data'],sub_category = values['pk_value'],location = values['pk_test']).filter(job_position__contains = searched)
        data={
            'jobs':jobs,
            'pk_test':values['pk_test'],
            'pk_data':values['pk_data'],
            'pk_value':values['pk_value'],
            'searched':searched
            }
        return render(request, 'temp/search_jobs.html',data)

