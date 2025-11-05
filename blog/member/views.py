from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def sign_up(request):
    # username = request.POST.get('username')
    # password1 = request.POST.get('password1')
    # password2 = request.POST.get('password2')

    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
            form.save()
            return redirect(settings.LOGIN_URL)


    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/accounts/login/')
    # else:
    #     form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)