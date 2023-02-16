from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html',{})

# Blog Page
def blog(request):
    posts = Post.objects.order_by('-post_date')
    # Get all the categories
    categories = Category.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts,'categories':categories})

# # Single Article Page
# def article_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     context = {
#         'post': post
#     }
#     return render(request, 'blog/article_details.html', context)

# Single Article Page with Add Comment form
def article_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.order_by('-date_added')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('article-detail', pk=post.pk)
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comment': comment,
        'form': form
    }
    return render(request, 'blog/article_details.html', context)

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('article_detail', pk=comment.post.pk)
    else:
        return render(request, 'blog/article_details.html', {'comment': comment})

class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'

class DeletePostView(generic.DeleteView):
    model = Post
    template_name ='blog/delete_post.html'
    success_url= reverse_lazy('blog')


def CategoryView(request,cat):
    #cat = cat.replace("-"," ")
    category_posts = Post.objects.filter(category=cat)
    return render(request, 'blog/category.html', {'cat':cat.title(),'category_posts':category_posts})


def contact(request):
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'contact/index.html', {})

def about(request):
    return render(request, 'about/index.html', {})


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')
