from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Feedback
from .forms import RegisterUserForm, UserAuthForm

def home(request):
    if request.method == 'POST':

        if 'login' in request.POST:
            login_form= UserAuthForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('home')
        
        if 'signup' in request.POST:
            signup_form = RegisterUserForm(request.POST)
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
        signup_form = RegisterUserForm()
        login_form = UserAuthForm()
    else:
        signup_form = RegisterUserForm()
        login_form = UserAuthForm()
    return render(request, 'accounts/home.html', {'login_form': login_form, 'signup_form': signup_form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
