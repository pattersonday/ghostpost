from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone


from .models import BoastsAndRoasts
from .forms import BoastsAndRoastsAddForm


def index(request):
    html = 'index.html'

    boastsandroasts = BoastsAndRoasts.objects.all()

    return render(request, html, {'boastsandroasts': boastsandroasts})


def BoastsAndRoastsFormView(request):
    html = 'boastandroast_form.html'

    if request.method == 'POST':
        form = BoastsAndRoastsAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            BoastsAndRoasts.objects.create(
                # boasts_or_roasts=data['boasts_or_roasts'],
                is_boast=data['is_boasts'],
                content=data['content'],
                upvote=data['upvote'],
                downvote=data['downvote'],
                post_data=timezone.now()
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = BoastsAndRoastsAddForm()

    return render(request, html, {'form': form})
