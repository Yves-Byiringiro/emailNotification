from django.shortcuts import render
from .models import ReportType

def returning_same(request):
    user_email = ReportType.objects.all()

    context = {
        'user_email':user_email
    }
    return render( request,'report/home.html', context)