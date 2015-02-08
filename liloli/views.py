from django.contrib import messages
from django.shortcuts import render

from liloli.forms import EmailSubscriptionForm

from ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='10/h')
def landing(request):
    form = EmailSubscriptionForm(request.POST or None)
    if getattr(request, 'limited', False):
        messages.error(request, "You have been doing that too much. \
                       If you wait, you can get another soon.")
    else:
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
