from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def calculator(request):
    v1=request.POST["t1"]
    v2=request.POST["t2"]
    op=request.POST["top"]
    print(op)
    i=0
    j=0
    k=0
    try:
        i=int(v1)
        j=int(v2)
    except(ValueError):
        return render(request,'input.html')
    if op == 'add':
        k = i+j
        return HttpResponse(k)
    elif op == "sub":
        k = i-j
        return HttpResponse(k)
    elif op == 'mul':
        k = i*j
        return HttpResponse(k)
    else:
        try:
            k = i/j
            return HttpResponse(k)
        except(ZeroDivisionError):
            return render(request,'input.html')
