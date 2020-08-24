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
from .forms import cmtform
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
    comments=comment.objects.filter(active=True).filter(post=post)
    if request.method=='POST':
        comment_form=cmtform(request.POST or None)
        try:
            if comment_form.is_valid():
                name= comment_form.cleaned_data.get('name')
                email= comment_form.cleaned_data.get('email')
                body=comment_form.cleaned_data.get('body')
                comment_form1 = comment.objects.create(
                    post=post,
                    name=name,
                    email=email,
                    body=body,
                )
                #contact_me.save()
                #return redirect('blog:post-detail')
        except ObjectDoesNotExist:
            messages.error(self.request, "fill the form correctly")
            #return redirect("core:contact")
    else:
        comment_form=cmtform()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'comment_form': cmtform})
