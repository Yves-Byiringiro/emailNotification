from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from EmailConfirmationP.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from report import models
from django.contrib.auth.models import User


def all_emails():
    minutes = ['byives21@gmail.com','niyoeri6@gmail.com']
    yyy = models.ReportType.objects.all()

    for y in yyy:
        minutes.append(y.owner.email)
        print('======================================')

    return minutes




def mailweek( *args, **kwargs):
    all_emails()
    reports = models.ReportType.objects.all()

    for report in reports:
        print('=============')
        print(report.owner)
        print('==============')
    subject = "Welcome "
    message = 'New Report has been added successfully !!!'
    send_mail(subject, message, EMAIL_HOST_USER,all_emails())

    return None


def mailweeky( *args, **kwargs):
    all_emails()
    subject = "Welcome "
    message = 'New Report has been added successfully uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu !!!'
    send_mail(subject, message, EMAIL_HOST_USER,all_emails())

    return None


    
def start():
    t = all_emails()
    scheduler = BackgroundScheduler()
    scheduler.add_job(mailweek, 'interval', minutes=1)
    scheduler.add_job(mailweeky, 'interval', minutes=2)
    scheduler.start()

