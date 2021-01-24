from django.shortcuts import render
from footer.models import Info
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
def contact(request):
    details=Info.objects.last()
    if request.method == 'POST':
        name=request.POST.get('name')
        mail=request.POST['mail']
        subject=request.POST['subject']
        message=request.POST['messages']
        send_mail(
            subject,
            f"name is {name} mail is {mail} subject of message {subject} message contain {message} \n thanks",
            mail,
            [EMAIL_HOST_USER],
            fail_silently=False,
            )
    return render(request,'contact/contact.html',{'details':details})