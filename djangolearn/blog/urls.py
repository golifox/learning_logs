"""Defines URL patterns for blog."""
from django.contrib import admin
from django.urls import path, include

from . import views

app_name= 'blog'

urlpatterns = [
    # API urls
    #path('', include('myapi.urls')),

    # Home page.
    path('', views.index, name='index'),

    # Page that showing all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new Topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),

    # Page for editing entries
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
]   
