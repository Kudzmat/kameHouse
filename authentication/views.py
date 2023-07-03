from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def user_login(request):
    """"
    form security
    if request.method == "POST":
    form = OwnerCreateForm(request.POST)
        if form.is_valid():
            form = form.save()
        else:
            form = OwnerCreateForm()
  return render(request, "vetoffice/owner_create_form.html", {"form":form})
    """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate username & passwords
        user = authenticate(request, username=username, password=password)
        if user is not None:  # if user data exists
            login(request, user)
            return redirect('profile')

        else:
            messages.error(request, 'Invalid Email or Password')  # user not found

    return render(request, 'authentication/login.html')


# new user registration
def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # password check
        if password == confirm_password:

            # username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This Username Is Already Registered')

            # email already exists
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This Email Is Already Registered')

            # all checks clear!
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('profile')

        # passwords do not match
        else:
            messages.error(request, 'Unsuccessful Registration, Passwords Do Not Match!')

    return render(request, 'authentication/registration.html')


def reset(request):
    return render(request, 'authentication/forgot.html')


# logging out
def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('login')
