from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpRequest

# # Create your views here.
# class UserLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('home')  # Replace 'home' with the name of the URL you want to redirect to after login

# Login 
def my_custom_login_view(request: HttpRequest):
    # Initialize an empty warning message
    warning_message = ''
    
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # Set a warning message for already logged-in users
        warning_message = 'You are already logged in.'

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if not request.user.is_authenticated:
                    login(request, user)
                    return redirect('some_success_url')  # Adjust this to where you want to redirect users
                else:
                    warning_message = 'You are already logged in.'
    else:
        form = AuthenticationForm()

    # Include the warning message in the context passed to the template
    context = {
        'form': form,
        'warning_message': warning_message,
    }
    return render(request, 'auth/login.html', context)

# succes redirect
def success_view(request):
    return redirect('home')

def my_custom_logout_view(request: HttpRequest):
    logout(request)
    # Add a logout message
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out.')
    # Redirect to the homepage
    return redirect('home')  # Make sure 'home' corresponds to the name of your homepage URL pattern.

