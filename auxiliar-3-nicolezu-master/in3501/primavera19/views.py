from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def formulario(request):
	return render(request, 'formulario.html')