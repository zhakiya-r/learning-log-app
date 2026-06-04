from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registers a new user"""
    if request.method != "POST":
        # Display an empty registration form
        form = UserCreationForm()
    else:
        # Processing the submitted form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to the home page
            login(request, new_user)
            return redirect("learning_logs:index")
        
    # Display an empty or invalid form
    context = {"form": form}
    return render(request, "registration/register.html", context)