from django.shortcuts import render

# Create your views here.
def htmlfile1(request):
    d={'name':'sree'}
    return render(request,'htmlfile1.html',d)