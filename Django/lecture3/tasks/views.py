from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    if "tasks" not in request.session: # if the user does not have an empty list of tasks in their session, create one.
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"],
    })


def add(request):
    if request.method == "POST":  # SERVER-SIDE VALIDATION
        form = NewTaskForm(request.POST)  # request.POST contains all the data that the user submitted.
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.sessions["tasks"].append(task)  # append the task submitted to the list of tasks in the user's session.
            return HttpResponseRedirect(reverse("tasks:index"))  # Redirects the user to the index page.
        else:
            return render(request, "tasks/add.html", {
                "form": form,
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm(), # creates a new instance of the NewTaskForm class.
    })

def add_form_not_working_yet(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm(), # creates a new instance of the NewTaskForm class.
    })
