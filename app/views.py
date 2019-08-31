from django.shortcuts import render, redirect
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def index(request):
    """
    View function to render the homepage
    """
    return render(request, 'all-templates/index.html')


def homepage(request):
    """
    View function to render the homepage
    """
    images = Image.all_images()
    return render(request, 'all-templates/home.html',{"images":images})


@login_required(login_url='/accounts/login/')
def display_images(request):
    images = Image.all_images()
    return render(request, 'all-templates/index.html', {"images": images})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profiles = Profile.get_by_id(profile.id)
    except:
        profiles = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    return render(request, 'all-templates/profile.html', {'images': images,"profile":profile,"profiles":profiles})


@login_required(login_url='/accounts/login/')
def upload_image(request):
    images = Image.all_images()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            upload.save()
            return redirect('profile', username=request.user)
    else:
        form = ImageForm()
    
    return render(request, 'all-templates/profile.html', {'form':form,'images':images})


@login_required(login_url='/accounts/login/')
def image_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            upload.save()
        return redirect('profile',username= request.user)

    else:
        form = ImageForm()
    return render(request, 'all-templates/upload.html', {"form": form})
