from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'Home - авторизация',
    }

    return render(request, 'users/login.html', context=context)


def registration(request):
    context = {
        'title': 'Home - регистрация',
    }

    return render(request, 'users/registration.html', context=context)


def profile(request):
    context = {
        'title': 'Home - кабинет',
    }

    return render(request, 'users/profile.html', context=context)



def logout(request):
    ...