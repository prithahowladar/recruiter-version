
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import UserInfo
from django.contrib.auth.forms import UserCreationForm
# Create your views here.from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm, UserInfoForm

# Create your views here.
def home(request):
    return HttpResponse("<h1>HOME PAGE</h1>")
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

class AltSignup(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'registration/altsignup.html'


@login_required
def userinfoview(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)

        if form.is_valid():
            userinfo = form.save(commit = False)

            userinfo.user = request.user
            userinfo.save()

            return redirect("thanks")
    else:
        form = UserInfoForm()
        context = {"form":form}
        return render(request, "create_Userinfo.html", context)

def register(request):
    if request.method == "POST":
        form1 = UserCreateForm(request.POST)
        form2 = UserInfoForm(request.POST)
        if form1.is_valid() and form2.is_valid():

            user = form1.save()
            userinfo = form2.save(commit = False)

            userinfo.user = user
            userinfo.save()

            username  = form1.cleaned_data.get("username")
            password  = form1.cleaned_data.get("password1")

            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect("home")
    else:
        form1 = UserCreateForm()
        form2 = UserInfoForm()
        context = {"form1":form1, "form2":form2}
        return render(request, "register.html", context)
