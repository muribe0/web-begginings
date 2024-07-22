from django.shortcuts import render

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
        if entry in entries:  # if it is an exact match
            return visit_entry(request, entry)
        else: # if it is a partial match
            partial_matches = [e for e in entries if entry.lower() in e.lower()]
            return index(request, partial_matches)



def visit_entry(request, entry):

    entry_content = util.get_entry(entry)
    if entry_content is None:  # if the entry is not valid
        return render(request, "encyclopedia/error.html", {
            "title": entry})

    entry_content = markdown2.markdown(entry_content)  # convert it from md to html

    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "entry_content": entry_content,
    })

def visit_random_entry(request):
    entries = util.list_entries()
    return visit_entry(request, entries[randint(0, len(entries) - 1)])
