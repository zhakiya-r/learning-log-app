from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

def index(request):
    """Home page for the "Learning Logs" application"""
    return render(request, "learning_logs/index.html")

def topics(request):
    """Displays a list of topics"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics":topics}
    return render(request, "learning_logs/topics.html", context)

def topic(request, topic_id):
    """Displays a topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic":topic, "entries":entries}
    return render(request, "learning_logs/topic.html", context)

def new_topic(request):
    """Adds a new topic"""
    if request.method != "POST":
        # No data was submitted; an empty form is created
        form = TopicForm()
    else:
        # POST data submitted; process the data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")
    # Display an empty or invalid form
    context = {"form":form}
    return render(request, "learning_logs/new_topic.html", context)