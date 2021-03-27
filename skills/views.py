from django.shortcuts import render
from .models import ProgrammingKnowledge

# Create your views here.
def home(request):
    programming = ProgrammingKnowledge.objects.all()
    return render(request, 'homepage/main.html',{'skills': programming} )