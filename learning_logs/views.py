from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_entry(request, topic_id):
    """Adds a new entry for a specific topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # No data was submitted; an empty form is created
        form = EntryForm()
    else:
        # POST data submitted; process the data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)
    # Dsiplay an empty or invalid form
    context = {"topic":topic, "form":form}
    return render(request, "learning_logs/new_entry.html", context)

def edit_entry(request, entry_id):
    """Edits an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        # Initial request; the form is populated with the current entry's data
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process the data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic.id)
    context = {"entry":entry, "topic":topic, "form":form}
    return render(request, "learning_logs/edit_entry.html", context)