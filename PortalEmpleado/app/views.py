from django.shortcuts import render

# Create your views here.

def inicio_portal(request):
    return render(request, 'app/inicio_portal.html',{})
def login_usuario(request):
    return render(request, 'app/login_usuario.html',{})
def registro_usuario(request):
    return render(request, 'app/registro_usuario.html',{})