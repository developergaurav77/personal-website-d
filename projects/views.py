from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.
def projects(request):
    project = Projects.objects.order_by('-date')
    return render(request,'projects/project.html',{'projects':project})

def projectdetails(request,project_id):
    projects = get_object_or_404(Projects, pk=project_id)
    return render(request,'projects/details.html',{'project_ids':projects})   