from django.shortcuts import render


def Test(request):
    return render(request,'test.html')