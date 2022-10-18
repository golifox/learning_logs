from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404


from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """The home page for Blog."""
    return render(request, 'blog/index.html')


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blog/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show one selected topic."""
    topic = Topic.objects.get(id=topic_id)
    # Except the topic belongs to the current user.
    if topic.owner != request.user:
        return Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blog/topic.html', context) 


@login_required
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


@login_required
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
            return redirect('blog:topic', topic_id=topic_id)
            
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'blog/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blog/edit_entry.html', context)
