from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import MascotaForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def iniciarSesion(request):
    if request.method=="GET":
        return render(request, "login.html",{
            "form": AuthenticationForm,
        })
    else:
        try:
            user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect("/home")
            else:
                return render(request, "login.html",{
                "form": AuthenticationForm,
                "msg": "El usuario o contraseña es incorrecto"
            })
        except Exception as e:
            return render(request, "login.html",{
                "form": AuthenticationForm,
                "msg": "Hubo un error{e}"
            })

def home(request):
    return render(request,"home.html",{
        "msg":"Bienvenido usuario"
    })

def registro(request):
    if request.method == "GET":
        return render(request,"registro.html",{
        "form": UserCreationForm
    })
    else:
        #Aqui tenemos nuestro POST
        req=request.POST
        if req['password1']==req['password2']:
            try:
                user = User.objects.create_user(
                    username=req['username'],
                    password=req['password1']
                )
                user.save()
                login(request,user)
                return redirect("/home")
            except IntegrityError as ie:
                return render(request,"registro.html",{
                    "form": UserCreationForm,
                    "msg": "Este usuario ya existe"
                })
            except Exception as e:
                return render(request,"registro.html",{
                    "form": UserCreationForm,
                    "msg": f"Hubo un error{e}"
                })
                
            
def cerrarsesion(request):
    logout(request)
    return redirect("/")

@login_required
def mascota(request):
    if request.method=="GET":
        return render(request, "mascota.html",{
                    "form": MascotaForm
                })
    else:
        try: 
            form=MascotaForm(request.POST)
            if form.is_valid():
                nuevo=form.save(commit=False)
                if request.user.is_authenticated:
                    nuevo.usuario=request.user
                    nuevo.save()
                    return redirect("/home")
                else:
                    return render(request, "mascota.html",{
                        "form": MascotaForm,
                        "msg":"Debe de autenticarse"
                    })
            else:
                return render(request, "mascota.html",{
                        "form": MascotaForm,
                        "msg": "Esta mascota no es valida"
                    })
        except Exception as e:
            return render(request, "mascota.html",{
                        "form": MascotaForm,
                        "msg": f"Error de autenticacion{e}"
                    })
                    