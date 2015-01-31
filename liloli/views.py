from django.contrib import messages
from django.shortcuts import render

from liloli.forms import EmailSubscriptionForm


def landing(request):
    form = EmailSubscriptionForm(request.POST or None)
    if form.is_valid():
        if form.save(request=request):
            msg = "Thank you for signing up! \
                You will get your coupon a week before opening!"
        else:
            msg = "You already signed up silly, but we love your enthusiasm!"
        messages.success(request, msg)
    context = {
        'form': form,
    }
    return render(request, 'landing.html', context)
