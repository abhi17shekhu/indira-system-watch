from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
	new = Post.objects.filter().order_by('-published_date')[:16:1]
	return render(request, 'app1/index.html', { 'new' : new } )
