from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Attachment, Thread, Message
import os


#auth
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu istifadəçi adı artıq mövcuddur')
            return redurect('register')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('project_list')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,  password=password)
        if user:
            login(request, user)
            return redirect('project_list')
        messages.error(request, 'Yanlış istifadəçi adı və ya şifrə')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')



#projects
@login_required
def project_list(request):
    projects = Project.objects.filter(members=request.user) | Project.objects.filter(admin=request.user)
    projects = projects.distinct()
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description', '')
        project = Project.objects.create(name=name, description=description, admin=request.user)
        project.members.add(request.user)
        return redirect('project_detail', pk=project.pk)
    return render(request, 'project_create.html')

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    is_member = request.user in project.members.all() or request.user == project.admin
    if not is_member:
        return redirect('project_list')
    return render(request, 'project_detail.html', {'project': project})


#attachments
@login_required
def attachment_create(request, pk):
    project = get_object_or_404(Project, pk=pk)
    is_member = request.user in project.members.all() or request.user == project.admin
    if not is_member:
        return redirect('project_list')
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            ext = os.path.splitext(file.name)[1].lower().replace('.', '')
            Attachment.objects.create(project=project, uploaded_by=request.user, file=file, format=ext)
        return redirect('project_detail', pk=pk)
    return render(request, 'attachment_create.html', {'project': project})


@login_required
def attachment_destroy(request, pk):
    attachment = get_object_or_404(Attachment, pk=pk)
    project_pk = attachment.project.pk
    is_member = request.user in attachment.project.members.all() or request.user == attachment.project.admin
    if is_member:
        attachment.delete()
    return redirect('project_detail', pk=project_pk)


# THREADS
@login_required
def thread_create(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.admin:
        return redirect('project_detail', pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        Thread.objects.create(project=project, title=title, created_by=request.user)
        return redirect('project_detail', pk=pk)
    return render(request, 'thread_create.html', {'project': project})


@login_required
def thread_edit(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.user != thread.project.admin:
        return redirect('project_detail', pk=thread.project.pk)
    if request.method == 'POST':
        thread.title = request.POST['title']
        thread.save()
        return redirect('project_detail', pk=thread.project.pk)
    return render(request, 'thread_edit.html', {'thread': thread})


@login_required
def thread_destroy(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    project_pk = thread.project.pk
    if request.user == thread.project.admin:
        thread.delete()
    return redirect('project_detail', pk=project_pk)


# MESSAGES
@login_required
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    is_member = request.user in thread.project.members.all() or request.user == thread.project.admin
    if not is_member:
        return redirect('project_list')
    return render(request, 'thread_detail.html', {'thread': thread})


@login_required
def message_create(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    is_member = request.user in thread.project.members.all() or request.user == thread.project.admin
    if not is_member:
        return redirect('project_list')
    if request.method == 'POST':
        content = request.POST['content']
        Message.objects.create(thread=thread, content=content, created_by=request.user)
        return redirect('thread_detail', pk=pk)
    return render(request, 'message_create.html', {'thread': thread})


@login_required
def message_edit(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.user != message.created_by:
        return redirect('thread_detail', pk=message.thread.pk)
    if request.method == 'POST':
        message.content = request.POST['content']
        message.save()
        return redirect('thread_detail', pk=message.thread.pk)
    return render(request, 'message_edit.html', {'message': message})


@login_required
def message_destroy(request, pk):
    message = get_object_or_404(Message, pk=pk)
    thread_pk = message.thread.pk
    if request.user == message.created_by:
        message.delete()
    return redirect('thread_detail', pk=thread_pk)