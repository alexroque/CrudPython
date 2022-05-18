from django.shortcuts import render, redirect
from Crud.forms import CarroForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = CarroForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')