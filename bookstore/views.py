from django.shortcuts import render, redirect
# Django authentication libraries
from django.contrib.auth import authenticate, login, logout, get_user_model
# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# define a function view called login_view that takes a request from user


def login_view(request):
    # Handle demo login
    if request.method == 'POST' and 'demo_login' in request.POST:
        User = get_user_model()
        try:
            demo_user = User.objects.get(username='demo_user')
            login(request, demo_user)
            messages.success(request, 'Logged in as demo user')
            return redirect('books:home')
        except User.DoesNotExist:
            messages.error(request, 'Demo user not found. Please contact support.')
            return redirect('login')
    
    # Initialize form and error message
    error_message = None
    form = AuthenticationForm()

    # Handle regular login
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():                                
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('books:home')
            else:
                error_message = 'Invalid credentials'
        else:
            error_message = 'Invalid form submission'

    # Prepare context for template
    context = {
        'form': form,
        'error_message': error_message,
        'show_demo_button': True  # Flag to show demo button in template
    }
    #load the login page using "context" information
    return render(request, 'auth/login.html', context)

#define a function view called logout_view that takes a request from user
def logout_view(request):                                 
    logout(request)             #the use pre-defined Django function to logout
    return redirect('login')    #after logging out go to login form (or whichever page you want)