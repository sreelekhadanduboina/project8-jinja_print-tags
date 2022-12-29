from django.shortcuts import render

# Create your views here.
def htmlfile2(request):
    d={'name':'lekha'}
    return render(request,'htmlfile2.html',d)