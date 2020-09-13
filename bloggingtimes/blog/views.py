from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View,CreateView
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Post,comment
from .forms import cmtform,blogform,newblog
from django.http import HttpResponse
class home(View):
    def get(self, *args, **kwargs):
        post=Post.objects.order_by('-date_posted').filter(passed_by_mentor=True)
        context = {
            'blogs': post
        }
        return render(self.request, "index.html", context)

#class Postcreateview(CreateView):
    '''
    model=Post
    fields=['title','content','thumnail_image','main_img']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


'''
@login_required
def Postcreateview(request):
    return render(request,'new-blog-post.html')

@login_required
def new_all_blogs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            blogContent = request.POST['blog-content']
            main_img=request.POST['cover-images']
            thum_img=request.POST['thum-images']
            try:
                user_logged=request.user
               
            except:
                return HttpResponse('user logged in not detected')
            try:
                #user1 = Post(author=request.user,title=title,main_img='',thumnail_img='')
                #print(user1)
                create_blog=Post.objects.create(
                    title=title,content=blogContent,author=user_logged,main_img=main_img,thumnail_img=thum_img
                )
            except:
                return HttpResponse('Error in object create')
            #try:
             #   user.save() 
            #except:
             #   return HttpResponse('error in save')
            return HttpResponse('test.html')

class all_blogs(ListView):
    model = Post
    template_name = 'all-blogs-page.html'  
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 6
    def get_queryset(self):
       result = super(all_blogs, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Post.objects.filter(title__contains=query)
          result = postresult
       else:
           result = Post.objects.order_by('-date_posted')
       return result


def PostDetailView(request,pk):
    template_name='single-blog-page.html'
    post=get_object_or_404(Post,id=pk)
    comments=comment.objects.filter(active=True).filter(post=post).order_by('-created_on')
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
