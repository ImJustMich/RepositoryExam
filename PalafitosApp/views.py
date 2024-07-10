from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Cliente
from .models import Donacion

def home(request):
    return render(request, "Inicio.html")

def registrarCliente(request):
    if request.method == 'POST':
        rut = request.POST['txtRut']
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        telefono = request.POST['numtelefono']
        correo = request.POST['txtCorreo']
        fecha_viaje_str = request.POST['fecha_viaje']
        fecha_viaje = datetime.strptime(fecha_viaje_str, '%Y-%m-%d').date()
        metodoPago = request.POST['metodo_pago']
        categoria = request.POST['categoria']


        cliente = Cliente.objects.create(rut=rut,nombre=nombre,apellido=apellido,telefono=telefono,email=correo,fecha_viaje=fecha_viaje,metodoPago=metodoPago,categoria=categoria)
        return render(request, 'Viajar.html')
        
def inicio(request):
    return render(request, 'inicio.html')

def viajar(request):
    return render(request, 'viajar.html')

def galeria(request):
    return render(request, 'galeria.html')

def donaciones(request):
    return render(request, 'Donaciones.html')

def RegistrarDonacion(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        correo = request.POST['txtCorreo']
        monto = request.POST['numMonto']

        donacion = Donacion.objects.create(nombre=nombre,apellido=apellido,email=correo,monto=monto)
        return render(request, 'Donaciones.html')

def cuidadosRiesgos(request):
    return render(request, 'cuidadosRiesgos.html')