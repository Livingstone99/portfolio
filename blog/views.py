from django.shortcuts import render
from .models import Blog

# Create your views here.
def allblogs(request):
    titles = Blog.objects.all
    return render(request, 'blog/allblogs.html', {"titles":titles})