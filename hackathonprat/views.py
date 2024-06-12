from django.shortcuts import render


def inicio(request):
    contexto1={
        "user": "stv1",
     }
    print("recuest:", request)
    print("has llamado a inicio")
    return render (request,"inicio.html", context=contexto1)