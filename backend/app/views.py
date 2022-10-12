import logging

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@login_required
@require_http_methods(["GET"])
def test_send_email(request):
    logger.debug(
        f"Test for sending email: from {settings.DEFAULT_FROM_EMAIL} to {settings.DEFAULT_FROM_EMAIL}"
    )
    send_mail(
        "Testing send email",
        f"Testing send email from user {request.user}",
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )

    logger.debug(
        f"Email sent: from {settings.DEFAULT_FROM_EMAIL} to {settings.DEFAULT_FROM_EMAIL}"
    )

    return HttpResponse(status=200)
