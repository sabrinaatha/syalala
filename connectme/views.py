from urllib.parse import urlencode

from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.urls import reverse

from .models import GetInTouch


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'


def connect(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    name = request.POST.get('name') or request.POST.get('full_name') or ''
    email = request.POST.get('email') or request.POST.get('email_address') or ''
    subject = request.POST.get('subject') or ''
    message = request.POST.get('message') or ''

    if not name or not email or not message:
        if is_ajax(request):
            return JsonResponse({'success': False, 'error': 'Name, email and message are required.'}, status=400)
        return redirect(f"{reverse('home')}?contact=error#contact")

    try:
        entry = GetInTouch.objects.create(
            full_name=name,
            email_address=email,
            subject=subject,
            message=message,
        )
    except Exception:
        if is_ajax(request):
            return JsonResponse({'success': False, 'error': 'Could not save message.'}, status=500)
        return redirect(f"{reverse('home')}?contact=error#contact")

    # send notification email
    try:
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'no-reply@localhost')
        mail_subject = f"Website contact: {subject or 'No subject'}"
        mail_message = f"From: {name} <{email}>\n\n{message}"
        send_mail(mail_subject, mail_message, from_email, ['sabrinaathashania@gmail.com'], fail_silently=False)
    except Exception as e:
        if is_ajax(request):
            print(f"Email sending failed: {e}")
            return JsonResponse({'success': True, 'message': 'Saved but failed to send email.'})
        return redirect(f"{reverse('home')}?contact=partial#contact")

    if is_ajax(request):
        return JsonResponse({'success': True, 'message': 'Message sent and saved. Thank you!'})
    return redirect(f"{reverse('home')}?contact=success#contact")
