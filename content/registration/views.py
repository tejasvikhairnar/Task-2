from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return redirect('register')
    else:
        form = RegistrationForm()
    form = RegistrationForm()

    return render(request,'index.html',{'form':form})
