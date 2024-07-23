from django.shortcuts import render, redirect

from . import util

import markdown2
from random import randint


def index(request, entries=None):
    entries = util.list_entries() if entries is None else entries
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def search(request):
    if request.method == "POST":
        entry = request.POST.get("q")
        entries = util.list_entries()
        for e in entries:
            if entry.lower() == e.lower():
                return redirect(visit_entry, entry=e)
        else:  # if it is a partial match
            partial_matches = [e for e in entries if entry.lower() in e.lower()]
            return index(request, partial_matches)



def visit_entry(request, entry):

    entry_content = util.get_entry(entry)
    if entry_content is None:  # if the entry is not valid
        return render(request, "encyclopedia/error.html", {
            "title": entry,
            "error_message": "Entry not found",
        })

    entry_content = markdown2.markdown(entry_content)  # convert it from md to html

    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "entry_content": entry_content,
    })

def visit_random_entry(request):
    entries = util.list_entries()
    return redirect(visit_entry, entry=entries[randint(0, len(entries) - 1)])


def create_entry(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if util.get_entry(title) is not None:  # if the entry already exists
            return render(request, "encyclopedia/error.html", {
                "title": title,
                "error_message": "The entry already exists",
            })

        # else, redirect to its page freshly created
        util.save_entry(title, content)
        return redirect(visit_entry, entry=title)

    return render(request, "encyclopedia/new_entry.html")

def edit_entry(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect(visit_entry, entry=title)

    return render(request, "encyclopedia/edit_entry.html", {
        "title": title,
        "content": util.get_entry(title),
    })