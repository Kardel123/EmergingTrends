from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PostForm
from .models import Post

def home_view(request):
    return render(request, 'home.html')

def item_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'item_detail.html', {'post': post})

def create_item_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')