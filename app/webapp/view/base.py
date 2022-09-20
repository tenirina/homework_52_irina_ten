from django.shortcuts import render

from webapp.models import ToDo


def index_view(request):
    to_does = ToDo.objects.all()
    context = {
        "to_does": to_does
    }
    return render(request, "index.html", context)
