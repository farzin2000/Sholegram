from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from authsystem.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as AuthUser


# Create your views here.

def index_page(request):
    print(request.user.id)
    print("ajaaab")
    return render(request, 'index.html')


class AuthUserCreate(CreateView):
    model = AuthUser
    fields = ['username', 'password', 'email']

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = form.save(commit=True)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return super(AuthUserCreate, self).form_valid(form)


class MyUserCreate(CreateView):
    model = User
    fields = ['gender', 'avatar']

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        print(self.request.user)
        return super(MyUserCreate, self).form_valid(form)


def logout_user(request):
    logout(request)
    return redirect("/")


def login_user(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/main")
            else:
                return render(request, 'user_not_active.html')

        else:

            return render(request, 'invalid.html')
    else:
        return render(request, 'login.html')


