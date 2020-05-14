from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# import message module
from django.contrib import messages
# import shortcuts here.
from django.shortcuts import redirect

# Create your views here.

def register_view(request):
    # instance of user creation form incase request is post/not
    if request.method == 'POST':
        # create form with posted data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the form
            form.save()
            # fetch username from from
            username = form.cleaned_data.get('username')
            # flash message if success,
            messages.success(request, f'Account created for {username}!') 
            return redirect('home')
    else:
        # create form instance if request not post
        form = UserCreationForm()
    # render the form
    return render(request, 'user/register.html', {"form": form})


def login_view(request):
    pass
    return render(request, 'user/login.html')

