from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def obesity_causes(request):
    return render(request, 'procedimiento.html')

def obesity_prevention(request):
    return render(request, 'prevention.html')

def obesity_statistics(request):
    return render(request, 'obesity_statistics.html')

def healthy_tips(request):
    return render(request, 'healthy_tips.html')
