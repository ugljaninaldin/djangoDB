from django.shortcuts import render
from .models import Member

# Create your views here.
def home(request):
    all_members = Member.objects.all
    return render(request, "website/home.html", {"members": all_members})