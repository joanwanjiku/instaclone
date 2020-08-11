from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


# Create your views here.
def home(request):
    all_posts = Post.get_all_posts()
   
    context = {
        'posts': all_posts,
    }
    return render(request, 'instaposts/index.html', context)

class PostDetailView(DetailView):
    model = Post

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['desc', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def add_comment(request, post_id):
    post = Post.objects.filter(pk=post_id)
    all_posts = Post.get_all_posts()   
    context = {
        'posts': all_posts,
    }
    if request.method == 'POST':
        print('hi')
        content = request.POST.get('comment')
        print(content)
        comment_inst = Comment(content=content, post_id=post_id)      
        comment_inst.save()  
        return redirect('welcome')
        
    return render(request, 'instaposts/index.html', context)
        