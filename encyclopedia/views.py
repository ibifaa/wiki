from django.shortcuts import render



from . import util
from .models import Post



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html",{ 
        "entries":util.get_entry()
        
    } )

    model = Post
    template_name = 'entry.html'

