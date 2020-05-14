from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_view(request):
    # instance of user creation form incase request is post/not
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            # fetch username from from
            username = form.cleaned_data.get('username')
    else:
        # create form instance if request not post
        form = UserCreationForm()
    # render the form
    return render(request, 'user/register.html', {"form": form})
