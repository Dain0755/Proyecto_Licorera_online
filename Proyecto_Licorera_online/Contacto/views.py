from cmath import cos
import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Contacto.models import Contactos
from inventario.models import Productos
from shop.views import shoop

# Create your views here.


def Datos_Entrega(request, pk):
    producto = Productos.objects.get(id=pk)
    return render (request, "plantilla.html", {{"producto":producto}})
    

def Enviar_datos(request):
    if request.method=="POST":

        nombre_apellido = request.POST["nombres"]
        id = request.POST["id"]
        correo = request.POST["correo"]
        Direccion = request.POST["Direccion"]
        departamento = request.POST["Depa"]
        ciudad = request.POST["ciudad"]
        telefono = request.POST["telefono"]
        costo = request.POST["costo"]
        nombre_pro = request.POST["nombre_producto"]
        data = Contactos(name=nombre_apellido, id=id, email= correo, adress=Direccion, local=departamento, city=ciudad, cellphone=telefono, cost=costo, product_name=nombre_pro )
        data.save()

        return redirect('/shop/')
    
    else:

        return render (request, "plantilla.html")

