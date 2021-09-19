from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm, DocumentForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from .models import Document


def loginView(request):
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        user = authenticate(username = u, password = p)
        if user is not None:
            login(request, user)
            return redirect('show')
        else:
            messages.error(request, 'Invalid credentials')

    template_name = 'Account/login.html'
    context = {}
    return render(request, template_name, context)

def registerView(request):
    form = UserForm()
    print('before POST')
    if request.method == 'POST':
        print('After POST')
        form = UserForm(request.POST)
        print('after request.POST')
        if form.is_valid():
            print('valid form')
            form.save()
            return redirect('login')
    template_name = 'Account/register.html'
    context = {'form':form}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login')

def homeView(request):
    template_name = 'Account/home.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='login')
def showView(request):
    view = Document.objects.all()
    template_name = 'Account/show.html'
    context = {'view': view}
    return render(request, template_name, context)

def changePassword(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Your password was successfully Updated')
            return redirect('login')
        else:
            messages.error(request, 'Please check your password once')
    template_name = 'Account/change_password.html'
    context = {'form':form}
    return render(request, template_name, context)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'Account/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'Account/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = DocumentForm()
    return render(request, 'Account/model_form_upload.html', {
        'form': form
    })