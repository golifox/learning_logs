from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


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
