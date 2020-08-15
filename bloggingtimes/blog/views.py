from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Post
class home(View):
    def get(self, *args, **kwargs):
        post=Post.objects.order_by('-date_posted')
        context = {
            'blogs': post
        }
        return render(self.request, "index.html", context)
