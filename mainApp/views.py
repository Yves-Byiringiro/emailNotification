from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mainApp.forms import SignUpForm
from django.core.mail import send_mail

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            subject = 'Thank you so much'
            message = 'Welcome to Yves App, I really appreciate'
            from_email = 'settings.EMAIL_HOST_USER'
            to_list = ['save_it.email']

            send_mail(subject,message,from_email, to_list, fail_silently=False)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'mainApp/signup.html', {'form': form})

def home(request):
    return render(request, 'mainApp/home.html')




from django.core.mail import send_mail



# send_mail(
#     'Hello user',
#     'Hello user how are you doing?',
#     'byives21@gmail.com',
#     ['byiringiroyves127@gmail.com'],
#     fail_silently=True
# )