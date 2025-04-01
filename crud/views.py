from django.shortcuts import render

def obesity_home(request):
    return render(request, 'obesity_home.html')

def obesity_causes(request):
    return render(request, 'obesity_causes.html')

def obesity_prevention(request):
    return render(request, 'obesity_prevention.html')

def obesity_statistics(request):
    return render(request, 'obesity_statistics.html')

def healthy_tips(request):
    return render(request, 'healthy_tips.html')
