from django.shortcuts import render, HttpResponse
from .models import Feedback


def main(request):
    return render(request, 'home/index.html')


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Feedback(name=name, email=email, subject=subject,
                 messages=message).save()
        return HttpResponse(b'')
