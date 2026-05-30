from django.shortcuts import render

def index(request):
    """Home page for the "Learning Logs" application"""
    return render(request, "learning_logs/index.html")