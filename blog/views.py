from django.shortcuts import render
from .models import Post
# Create your views here.
def Home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def About(request):
    return render(request, 'blog/about.html')

