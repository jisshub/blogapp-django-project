from django.shortcuts import render
# import message module
from django.contrib import messages
# import shortcuts here.
from django.shortcuts import redirect
# import Register Form
from .forms import RegisterForm

# impot login_required decorators
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    # instance of user creation form incase request is post/not
    if request.method == 'POST':
        # create form with posted data
        form = RegisterForm(request.POST)
        if form.is_valid():
            # save the form
            form.save()
            # fetch username from from
            username = form.cleaned_data.get('username')
            # flash message if success,
            messages.success(request, f'Account created for {username}!') 
            return redirect('login')
    else:
        # create form instance if request not post
        form = RegisterForm()
    # render the form
    return render(request, 'user/register.html', {"form": form})

# user profile page
@login_required
def profile(request):
    return render(request, 'user/profile.html')

