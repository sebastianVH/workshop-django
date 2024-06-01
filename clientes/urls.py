from django.urls import path
from .views import verClientes,eliminarCliente,CrearCliente,actualizarCliente

urlpatterns = [
    path('listado/', verClientes,name='listado'), #=> (ruta, vista,name)
    path('eliminar/<int:id>/',eliminarCliente,name='eliminar'),
    path('crear/',CrearCliente,name='crear'),
    path('actualizar/<int:id>/',actualizarCliente,name='actualizar'),
]