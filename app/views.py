from django.conf import settings as config
from django.shortcuts import redirect


def home_view(request):
    """
        Redirect to client.
    """
    return redirect(config.CLIENT_URL)
