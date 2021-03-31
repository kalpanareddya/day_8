from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<h2 style='color:white;background-color:green'><center> Welcome to home</center></h2>")


def chk(request):
	return HttpResponse("<script>alert('hi good afternoon')</script><h2>welcome</h2>")


def homepage(request):
	return render(request,'html/homepage.html')

def lgn(re):
	return render(re,'html/login.html')

def reg(rt):
	return render(rt,'html/register.html')


