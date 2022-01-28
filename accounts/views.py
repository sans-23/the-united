from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Feedback

def home(request):
    if request.method == 'POST':

        if 'login' in request.POST:
            login_form= AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('home')
        
        if 'signup' in request.POST:
            signup_form = UserCreationForm(request.POST)
            print('debugging')
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('home')

        if 'feedback' in request.POST:
            feedback = request.POST.get('feedback')
            print(feedback)
            new_feedback = Feedback(feedback=feedback, user=request.user)
            new_feedback.save()
            return redirect('home')
        print('error')
        signup_form = UserCreationForm()
        login_form = AuthenticationForm()
    else:
        signup_form = UserCreationForm()
        login_form = AuthenticationForm()
    return render(request, 'accounts/home.html', {'login_form': login_form, 'signup_form': signup_form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
