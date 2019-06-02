from django.shortcuts import render
from .models import Contact
def index(request):
    if request.method== 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        c = Contact(email=email, message=message)
        c.save()
        return render(request, 'basicapp/index.htm')

    else:
        return render(request, 'basicapp/index.htm')
# Create your views here.
