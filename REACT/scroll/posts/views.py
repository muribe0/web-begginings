from django.http import JsonResponse
from django.shortcuts import render
import time

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')


def posts(request):

    # Get the start and end points
    start = int(request.GET.get('start', 0))
    end = int(request.GET.get('end', start + 9))

    # Generate list of posts
    data = [f"Post #{i}" for i in range(start, end + 1)]

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })