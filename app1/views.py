from django.shortcuts import render

# Create your views here.
def jinjaprint(request):

    d={'name':'hema','age':21}
    return render(request,'jinjaprint.html',context=d)
