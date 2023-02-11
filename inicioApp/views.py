from django.shortcuts import render
from .models import Trabajador,Usuario


# Create your views here.

def saludo(request):
    return render(request,"inicio.html",{})
def ps1(request):
    return render(request,"playstation-1.html", {})
def ps2(request):
    return render(request,"playstation-2.html", {})

def loginsesiondef(request):
    if request.method == 'GET':
        return render(request,"login.html",{})
    else:
        usuariostr = request.POST.get('userint')
        passwordstr = request.POST.get('passwordint')
        print(usuariostr,passwordstr)
        usuario = Usuario.objects.get(usuario=usuariostr,password=passwordstr)
        if not Usuario:
            return render(request,"login.html")
        else:
            trabajadoreslist = Trabajador.objects.values()
            print(trabajadoreslist)
            return render(request,"login.html",{"trabajadoreslist":trabajadoreslist})



