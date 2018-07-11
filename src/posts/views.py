# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post

# Create your views here.

#CRUD - CREATE REtrieve update delete
#list all the posts in view

def post_list_view(request):
    post_objects = Post.objects.all()
    context = {
        'post_objects': post_objects
    }
    return render(request, "posts/index.html", context)
