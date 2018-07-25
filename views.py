from django.shortcuts import render,redirect
from . models import AppUsers
from django.forms import ModelForm
from django.http import HttpResponse

# Create your views here.
class Loginform(ModelForm):
    class Meta:
        model = AppUsers
        fields = ['email', 'password']

class SignupForm(ModelForm):
    class Meta:
        model = AppUsers
        fields = ['Username','email','password']

def login(request):
    if request.method == 'POST':
        if request.POST.get("submit") == 'Log In':
            logform = Loginform(request.POST)
            if logform.is_valid():
                e = logform.cleaned_data["email"]
                p = logform.cleaned_data["password"]
                query_set = AppUsers.objects.filter(password=p,email=e)
                if not query_set:
                    return HttpResponse("Invalid Credentials")
        if request.POST.get("submit") == 'Sign Up':
            signform = SignupForm(request.POST)
            if signform.is_valid():
                signform.save()

        return HttpResponse("ufff")
    elif request.method == 'GET':
        logform = Loginform()
        signform = SignupForm()
        return render(request, template_name='login.html', context= {'logform': logform,'signform': signform })

