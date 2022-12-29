from django.shortcuts import render

# Create your views here.
def jinjaprint2(request):
    d={'name':'hema','course':'python'}
    return render(request,'jinjaprint2.html',d)
