from django.shortcuts import render
from.models import Job
from django.db.models import Sum

# Create your views here.
def home(request):
    jobs = Job.objects.all
    # bytes = len(Job.objects.filter(summary=request.user))
    # total_projects = Job.objects.filter(summary = id)

    return render(request, 'projects/better.html',{"jobs":jobs})

def project_detail(request, pk):
    projects = Job.objects.get(pk= pk)
    context = {
        'project': projects
    }
    return render(request, 'project/project_detail.html', context)