from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'singlepage/index.html')


texts = ["This is the first section", "This is the second section", "This is the third section"]


def section(request, section_id):
    if 1 <= section_id <= 3:
        return HttpResponse(texts[section_id - 1])
    else:
        return Http404("Section not found")

