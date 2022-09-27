"""Defines URL patterns for blog."""

from django.urls import path

from . import views

app_name= 'blog'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Page that showing all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new Topic.
    path('new_topic/', views.new_topic, name='new_topic'),
]
