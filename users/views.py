from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse


from traitlets import Instance



from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{user.username}, Вы успешно зарегестрированы и вошли в аккаунт")
                
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
        print(form.errors)
    else:
        form = UserLoginForm()        
            
    context = {
        'title': 'Home - авторизация',
        'form': form,
        
    }

    return render(request, 'users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()    
    
    
    context = {
        'title': 'Home - регистрация',
    }

    return render(request, 'users/registration.html', context=context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения в профиле вступили в силу")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ProfileForm(instance=request.user) 
    
    context = {
        'title': 'Home - кабинет',
        'form': form,
    }

    return render(request, 'users/profile.html', context=context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из акканта")
    auth.logout(request)
    
    return redirect(reverse('main:index'))