from django.shortcuts import render,redirect
from .models import Clientes
from .forms import ClienteForm

# Create your views here.
def verClientes(request):
    lista_clientes = Clientes.objects.all() #fuimos a la base de datos a pedir todos los usuarios
    contexto = {'clientes': lista_clientes} #crear la logica que permita al HTML junto con Python mostrar los datos
    return render(request,'listado.html',contexto) #renderizar (transformar los datos)


def eliminarCliente(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect('listado')

def CrearCliente(request):
    if request.method == 'GET':
        formulario = ClienteForm()
        contexto = {'form': formulario}
        return render(request,'crear.html',contexto)
    else:
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('listado')
    
def actualizarCliente(request, id):
    cliente = Clientes.objects.get(id=id)
    if request.method == 'GET':
        formulario = ClienteForm(instance=cliente)
        contexto = {'form': formulario}
        return render(request,'crear.html',contexto)
    else:
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
        return redirect('listado')