from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import User, Discussion
from .forms import UserCreationForm, LoginForm, DiscussionForm

from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserCreationForm()
    return render(request, 'user_create.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('discussion-list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def discussion_list(request):
    discussions = Discussion.objects.all()
    return render(request, 'discussion_list.html', {'discussions': discussions})


@login_required
def discussion_create(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST, request.FILES)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.user = request.user
            discussion.save()
            return redirect('discussion-list')
    else:
        form = DiscussionForm()
    return render(request, 'discussion_create.html', {'form': form})




@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
