from django.shortcuts import render

from blog.models import Post


def post_list(request):
    posts = Post.objects.all().order_by('published_dt')
    return render(request, 'blog/post_list.html', {'posts': posts})