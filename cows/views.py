from django.shortcuts import render
from cows.models import Recent
from cows.forms import InputForm
import subprocess
from django.shortcuts import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def recent_view(request):
    history = list(Recent.objects.all())
    history.reverse()
    return render(request, 'recent.html', {'history': history[0:10]})


def index(request):
    out = None
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p = data.get('phrase')
            cmd = subprocess.check_output(['cowsay', p],
                                          text=True
                                          )
            recents = Recent.objects.create(
                text=p, output=cmd)
            recents.save()
            return render(request, "index.html", {'form':InputForm(), 'output':cmd})
    form = InputForm()
    return render(request, 'index.html', {'form': form})
