from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm


def index(request):
    """The home page for Blog."""
    return render(request, 'blog/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blog/topics.html', context)

def topic(request, topic_id):
    """Show one selected topic."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blog/topic.html', context) 

def new_topic(request):
    """Add new topic."""
    if request.method != 'POST':
        # No data submitted. Create blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:topics')

    # Display blank or invalid form.
    context = {'form': form}
    return render(request, 'blog/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
 
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
            
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)