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
from .models import Post,comment
from .forms import commentform
class home(View):
    def get(self, *args, **kwargs):
        post=Post.objects.order_by('-date_posted').filter(passed_by_mentor=True)
        
        context = {
            'blogs': post
        }
        return render(self.request, "index.html", context)
def PostDetailView(request,pk):
    template_name='single-blog-page.html'
    post=get_object_or_404(Post,id=pk)
    comments=comment.objects.filter(active=True)
    new_comment=None
    if request.method=='POST':
        comment_form=commentform(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post=Post
            new_comment.save()
    else:
        comment_form=commentform()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})