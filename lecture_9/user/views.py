from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import auth


# Create your views here.
def login_page_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            auth.login(request, user)
            if user is not None:
                return redirect(to='index_page')
            else:
                form.add_error(field='username', error='Invalid password or username')
                return render(request, 'user/login.html', {'form': form})
        else:
            return render(request, 'user/login.html', {'form': form})


def register_page_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'user/register.html', {'form': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_data = auth.authenticate(request,
                                          username=form.data.get('username'),
                                          email=form.data.get('email'),
                                          password=form.data.get('password'))

            if auth_data is not None:
                auth.login(request, auth_data)
                return redirect(to='index_page')
            return render(request, 'user/register.html', {'form': form})
        else:
            return render(request, 'user/register.html', {'form': form})


def handle_logout(request):
    auth.logout(request)
    return redirect('/auth/login')

