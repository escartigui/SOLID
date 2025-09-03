import datetime
import os
from abc import ABC, abstractmethod
class Categoria:
    def __init__(self, idcategoria, nombre):
        self.idcategoria = idcategoria
        self.nombre = nombre

    def mostrar_categoria(self):
        return f"Categoria:{self.idcategoria} Nombre:{self.nombre}"
    def a_cadena(self):
        return f"{self.idcategoria}:{self.nombre}"
    @staticmethod
    def desde_cadena(cadena):
        idcategoria,nombre = cadena.strip().split(":")
        return Categoria(idcategoria, nombre)
class Productos:
    def __init__(self, idproducto, nombre, precio, idcategoria, stock=0):
        self.idproducto = idproducto
        self.nombre = nombre
        self.precio = precio
        self.idcategoria = idcategoria
        self.stock = stock

    def mostrar_producto(self):
        return f"Producto; Codigo: {self.idproducto},Nombre: {self.nombre},Precio: {self.precio},IdCategoria: {self.idcategoria},Stock: {self.stock}"
class Clientes:
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def mostrar_clientes(self):
        return f"Clientes: {self.nit}, {self.nombre}, {self.direccion}, {self.telefono}, {self.correo}"
    def a_cadena(self):
        return f"{self.nit}:{self.nombre}:{self.direccion}:{self.telefono}:{self.correo}"
    @staticmethod
    def desde_cadena(cadena):
        nit, nombre,direccion, telefono, correo = cadena.strip().split(":")
        return Clientes(nit,nombre,direccion,telefono,correo)
class Proveedores:
    def __init__(self, niti, nombre, direccion, telefono, correo, empresa):
        self.niti = niti
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.empresa = empresa

    def mostrar_proveedores(self):
        return f"Proveedores: {self.niti}, {self.nombre}, {self.direccion}, {self.telefono}, {self.correo}"
class Empleados:
    def __init__(self, idempleado, nombre, direccion, telefono, correo, puesto):
        self.idempleado = idempleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto

    def mostrar_empleados(self):
        return f"Empleado(s): {self.idempleado}, {self.nombre}, {self.direccion}, {self.telefono}, {self.correo}, {self.puesto}"
class Ventas:
    def __init__(self, idventas, fecha, nit, idempleado, total=0.0):
        self.idventas = idventas
        self.fecha = fecha
        self.nit = nit
        self.idempleado = idempleado
        self.total = total

    def mostrar_ventas(self):
        return f"Id Ventas:{self.idventas}, Fecha: {self.fecha}, Nit: {self.nit}, Total: {self.total}"
class DetalleVentas:
    def __init__(self, idetallevent, idventa, idproducto, cantidad, subtotal):
        self.idetallevent = idetallevent
        self.idventa = idventa
        self.idproducto = idproducto
        self.cantidad = cantidad
        self.subtotal = subtotal

    def mostrar_detalleventas(self):
        return f"Detalle Id:{self.idetallevent},Venta Id: {self.idventa},Id Producto: {self.idproducto},Cantidad: {self.cantidad},subtotal: {self.subtotal}"
class Compras:
    def __init__(self, idcompras, fecha, niti, total=0.0):
        self.idcompras = idcompras
        self.fecha = fecha
        self.niti = niti
        self.total = total

    def mostrar_compras(self):
        return f"Id Compra:{self.idcompras}, fecha: {self.fecha}, proveedor: {self.niti}, Total: {self.total}"
class DetalleCompras:
    def __init__(self, id_detallecompra, idcompras, idproducto, cantidad, costo_unitario, subtotal):
        self.id_detallecompra = id_detallecompra
        self.idcompras = idcompras
        self.idproducto = idproducto
        self.cantidad = cantidad
        self.costo_unitario = costo_unitario
        self.subtotal = subtotal

    def mostrar_detallecompra(self):
        return f"Detalle Id: {self.id_detallecompra},Compra Id: {self.idcompras},Producto: {self.idproducto},Cantidad: {self.cantidad},Costo Unicario: {self.costo_unitario},SubTotal: {self.subtotal}"
class IRepositorioCompras(ABC):
    @abstractmethod
    def agregar(self, compra):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, idcompras):
        pass
class IRepositorioVentas(ABC):
    @abstractmethod
    def agregar(self, venta):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, idventas):
        pass
class IRepositorioDetalleVentas(ABC):
    @abstractmethod
    def agregar(self, detalleventa):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, idetallevent):
        pass
class IRepositorioProveedores(ABC):
    @abstractmethod
    def agregar(self, proveedor):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, niti):
        pass
class IRepositorioCategorias(ABC):
    @abstractmethod
    def agregar(self, categoria):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, idcategoria):
        pass
class IRepositorioProductos(ABC):
    @abstractmethod
    def agregar(self, producto):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, idproducto):
        pass

    @abstractmethod
    def eliminar(self, idproducto):
        pass
class IRepositorioClientes(ABC):
    @abstractmethod
    def agregar(self, cliente):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, nit):
        pass
class IRepositorioEmpleados(ABC):
    @abstractmethod
    def agregar(self, empleado):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, idempleado):
        pass
class IRepositorioDetalleCompras(ABC):
    @abstractmethod
    def agregar(self, detalle_compra):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, id_detallecompra):
        pass
class RepositorioClientesMemoria(IRepositorioClientes):
    def __init__(self):
        self.clientes = {}

    def agregar(self, cliente):
        self.clientes[cliente.nit] = cliente

    def listar(self):
        return list(self.clientes.values())

    def obtener(self, nit):
        return self.clientes.get(nit)
class RepositorioCategoriasMemoria(IRepositorioCategorias):
    def __init__(self):
        self.categorias = {}

    def agregar(self, categoria):
        self.categorias[categoria.idcategoria] = categoria

    def listar(self):
        return list(self.categorias.values())

    def obtener(self, idcategoria):
        return self.categorias.get(idcategoria)
class RepositorioProductosMemoria(IRepositorioProductos):
    def __init__(self):
        self.productos = {}

    def agregar(self, producto):
        self.productos[producto.idproducto] = producto

    def listar(self):
        return list(self.productos.values())

    def obtener(self, idproducto):
        return self.productos.get(idproducto)

    def eliminar(self, idproducto):
        if idproducto in self.productos:
            del self.productos[idproducto]
            print("Productos eliminado")
        else:
            print("producto no encontrado")
class RepositorioProveedoresMemoria(IRepositorioProveedores):
    def __init__(self):
        self.proveedores = {}

    def agregar(self, proveedor):
        self.proveedores[proveedor.niti] = proveedor

    def listar(self):
        return list(self.proveedores.values())

    def obtener(self, niti):
        return self.proveedores.get(niti)
class RepositorioEmpleadosMemoria(IRepositorioEmpleados):
    def __init__(self):
        self.empleados = {}

    def agregar(self, empleados):
        self.empleados[empleados.idempleado] = empleados

    def listar(self):
        return list(self.empleados.values())

    def obtener(self, idempleado):
        return self.empleados.get(idempleado)
class RepositorioVentasMemoria(IRepositorioVentas):
    def __init__(self):
        self.ventas = {}
        self.id_counter = 0

    def agregar(self, venta):
        self.id_counter += 1
        venta.idventas = str(self.id_counter)
        self.ventas[venta.idventas] = venta

    def listar(self):
        return list(self.ventas.values())

    def obtener(self, idventas):
        return self.ventas.get(idventas)
class RepositorioDetalleVentaMemoria(IRepositorioDetalleVentas):
    def __init__(self):
        self.detalleventa = {}
        self.id_counter = 0

    def agregar(self, detalleventa):
        self.id_counter += 1
        detalleventa.idetallevent = str(self.id_counter)
        self.detalleventa[detalleventa.idetallevent] = detalleventa

    def listar(self):
        return list(self.detalleventa.values())

    def obtener(self, idetalle):
        return self.detalleventa.get(idetalle)
class RepositorioComprasMemoria(IRepositorioCompras):
    def __init__(self):
        self.compras = {}
        self.id_counter = 0

    def agregar(self, compra):
        self.id_counter += 1
        compra.idcompras = str(self.id_counter)
        self.compras[compra.idcompras] = compra

    def listar(self):
        return list(self.compras.values())

    def obtener(self, idcompras):
        return self.compras.get(idcompras)
class RepositorioDetalleComprasMemoria(IRepositorioDetalleCompras):
    def __init__(self):
        self.detalles = {}
        self.id_counter = 0

    def agregar(self, detalle_compra):
        self.id_counter += 1
        detalle_compra.id_detallecompra = str(self.id_counter)
        self.detalles[detalle_compra.id_detallecompra] = detalle_compra

    def listar(self):
        return list(self.detalles.values())

    def obtener(self, id_detallecompra):
        return self.detalles.get(id_detallecompra)
class ClientesService:
    def __init__(self, repo_clientes):
        self.repo_clientes = repo_clientes

    def agregar_cliente(self, cliente):
        self.repo_clientes.agregar(cliente)

    def listar(self):
        return self.repo_clientes.listar()

    def obtener(self, nit):
        return self.repo_clientes.obtener(nit)
class CategoriaService:
    def __init__(self, repo_categoria):
        self.repo_categorias = repo_categoria

    def agregar_categoria(self, categoria):
        if any(c.nombre == categoria.nombre for c in self.repo_categorias.listar()):
            print("Ya existe")
            return
        self.repo_categorias.agregar(categoria)

    def listar(self):
        return self.repo_categorias.listar()
class ProductoService:
    def __init__(self, repo_producto, repo_categoria):
        self.repo_producto = repo_producto
        self.repo_categoria = repo_categoria

    def agregar_producto(self, producto):
        if not self.repo_categoria.obtener(producto.idcategoria):
            print("Primero la categoria")
            return
        self.repo_producto.agregar(producto)
        print("Producto agregado")

    def listar(self):
        return self.repo_producto.listar()

    def obtener_producto(self, idproducto):
        return self.repo_producto.obtener(idproducto)

    def eliminar_producto(self, idproducto):
        producto = self.repo_producto.obtener(idproducto)
        if producto:
            self.repo_producto.eliminar(idproducto)
        else:
            print("producto no encontrado")

    def actualizar_producto(self, idproducto, nuevo_precio=None, nuevo_stock=None):
        producto = self.repo_producto.obtener(idproducto)
        if not producto:
            print("producto no encontrado")
            return
        if nuevo_precio is not None:
            producto.precio = nuevo_precio
        if nuevo_stock is not None:
            producto.stock = nuevo_stock
        print("Editado correctamente")
class ProveedorService:
    def __init__(self, repo_proveedor):
        self.repo_proveedor = repo_proveedor

    def agregar_proveedor(self, proveedor):
        self.repo_proveedor.agregar(proveedor)

    def listar(self):
        return self.repo_proveedor.listar()

    def obtener(self, niti):
        return self.repo_proveedor.obtener(niti)
class EmpleadoService:
    def __init__(self, repo_empleado):
        self.repo_empleado = repo_empleado

    def agregar_empleado(self, empleado):
        self.repo_empleado.agregar(empleado)

    def listar(self):
        return self.repo_empleado.listar()

    def obtener(self, idempleado):
        return self.repo_empleado.obtener(idempleado)
class VentaService:
    def __init__(self, repo_venta, repo_detalleventa, cliente_service, empleado_service, producto_service):
        self.repo_venta = repo_venta
        self.repo_detalleventa = repo_detalleventa
        self.cliente_service = cliente_service
        self.empleado_service = empleado_service
        self.producto_service = producto_service

    def agregar_productoaventa(self, idventas):
        venta_actual = self.repo_venta.obtener(idventas)
        if not venta_actual:
            print("Venta no existe")
            return
        self.producto_service.listar()
        idproducto = input("Ingrese el codigo del producto: ").strip()
        cantidad = int(input("Ingrese la cantidad: "))
        producto_aventa = self.producto_service.obtener_producto(idproducto)
        if not producto_aventa:
            print("Producto no existe")
            return
        if producto_aventa.stock < cantidad:
            print("no hay suficiente")
            return
        subtotal = cantidad * producto_aventa.precio
        producto_aventa.stock -= cantidad
        nuevo_detalle = DetalleVentas(None, idventas, idproducto, cantidad, subtotal)
        self.repo_detalleventa.agregar(nuevo_detalle)
        venta_actual.total += subtotal
        print(f"producto {producto_aventa.nombre}, agregado a la venta Id: {idventas}")

    def iniciar_venta(self):
        nit = input("Ingrese el nit del cliente: ").strip()
        if nit.upper() == "CF":
            pass
        else:
            cliente = self.cliente_service.obtener(nit)
            if not cliente:
                print("El cliente no existe, la venta no puede ser iniciada.")
                return None
        idempleado = input("Ingrese ID del empleado: ").strip()
        empleado = self.empleado_service.obtener(idempleado)
        if not empleado:
            print("El empleado no existe, la venta no puede ser iniciada.")
            return None

        idventas = None
        fecha_actual = datetime.datetime.now()
        nueva_venta = Ventas(idventas, fecha_actual, nit, idempleado)
        self.repo_venta.agregar(nueva_venta)
        print(f"Venta iniciada con éxito. ID: {nueva_venta.idventas}")
        return nueva_venta

    def agregar_producto_venta(self):
        pass

    def finalizar_venta(self):
        pass

    def gestionar_venta_completa(self):
        idempleado = input("Ingrese el ID del empleado: ").strip()
        empleado = self.empleado_service.obtener(idempleado)
        if not empleado:
            print("El empleado no existe. La venta no puede ser iniciada.")
            return

        nit = input("Ingrese el NIT del cliente (o 'CF' si no tiene): ").strip()
        if nit.upper() != "CF":
            cliente = self.cliente_service.obtener(nit)
            if not cliente:
                opcion = input("El cliente no existe. ¿Desea agregarlo? (si/no): ").strip().lower()
                if opcion == 'si':
                    self.agregar_un_cliente(nit)
                    cliente = self.cliente_service.obtener(nit)
                    if not cliente:
                        print("No se pudo agregar el cliente. La venta se iniciará con NIT 'CF'.")
                        nit = "CF"
                else:
                    print("Se iniciará la venta con NIT 'CF'.")
                    nit = "CF"

        idventas = None
        fecha_actual = datetime.datetime.now()
        nueva_venta = Ventas(idventas, fecha_actual, nit, idempleado)
        self.repo_venta.agregar(nueva_venta)
        print(f"ID de la venta: {nueva_venta.idventas}")

        while True:
            self.producto_service.listar()
            idproducto = input("Ingrese el código del producto (o '0' para finalizar): ").strip()

            if idproducto == '0':
                break

            producto_aventa = self.producto_service.obtener_producto(idproducto)
            if not producto_aventa:
                print("Producto no existe.")
                continue

            try:
                cantidad = int(input("Ingrese la cantidad: "))
                if producto_aventa.stock < cantidad:
                    print("No hay suficiente stock.")
                    continue

                subtotal = cantidad * producto_aventa.precio
                producto_aventa.stock -= cantidad
                nuevo_detalle = DetalleVentas(None, nueva_venta.idventas, idproducto, cantidad, subtotal)
                self.repo_detalleventa.agregar(nuevo_detalle)
                nueva_venta.total += subtotal
                print(f"Producto '{producto_aventa.nombre}' agregado a la venta. Total actual: {nueva_venta.total}")
            except ValueError:
                print("Cantidad o precio inválido. Intente de nuevo.")

        print(f"\nVenta finalizada. Total: {nueva_venta.total}")
class CompraService:
    def __init__(self, repo_compras, repo_detallecompras, proveedor_service, producto_service):
        self.repo_compras = repo_compras
        self.repo_detallecompras = repo_detallecompras
        self.proveedor_service = proveedor_service
        self.producto_service = producto_service

    def iniciar_compra(self):
        niti = input("Ingrese el nit del proveedor: ").strip()
        proveedor = self.proveedor_service.obtener(niti)
        if not proveedor:
            print("El proveedor no existe")
            return None
        idcompras = None
        fecha_actual = datetime.datetime.now()
        nueva_compra = Compras(idcompras, fecha_actual, niti)
        self.repo_compras.agregar(nueva_compra)
        print(f"Compra iniciada con éxito. ID: {nueva_compra.idcompras}")
        return nueva_compra

    def agregar_producto_a_compra(self, idcompras):
        compra_actual = self.repo_compras.obtener(idcompras)
        if not compra_actual:
            print("La compra no existe")
            return
        self.producto_service.listar()
        idproducto = input("Ingrese el codigo del producto: ").strip()
        cantidad = int(input("Ingrese la cantidad: "))
        costo_unitario = float(input("Ingrese el costo unitario: "))
        producto_acomprar = self.producto_service.obtener_producto(idproducto)
        if not producto_acomprar:
            print("Producto no existe")
            return
        subtotal = cantidad * costo_unitario
        producto_acomprar.stock += cantidad
        nuevo_detalle = DetalleCompras(None, idcompras, idproducto, cantidad, costo_unitario, subtotal)
        self.repo_detallecompras.agregar(nuevo_detalle)
        compra_actual.total += subtotal
        print(f"producto: {producto_acomprar.nombre}, agregado a la compra con ID: {idcompras}")

    def finalizar_compra(self):
        pass
class Ordenamiento:
    @staticmethod
    def por_nombre(productos):
        def funcion_nom(producto):
            return producto.nombre.lower()

        return sorted(productos, key=funcion_nom)

    @staticmethod
    def por_precio(productos):
        def funcion_precio(producto):
            return producto.precio

        return sorted(productos, key=funcion_precio)

    @staticmethod
    def por_stock(productos):
        def funcion_stock(producto):
            return producto.stock

        return sorted(productos, key=funcion_stock)
class RepositorioClientesArchivo(IRepositorioClientes):
    def __init__ (self, archivo_nombre = "Clientes.txt"):
        self.archivo_nombre = archivo_nombre
        self.clientes = {}
        self.cargar_datos()
    def cargar_datos(self):
        if not os.path.isfile(self.archivo_nombre):
            return
        with open(self.archivo_nombre, "r", encoding = 'utf-8') as f:
            for linea in f:
                cliente = Clientes.desde_cadena(linea)
                self.clientes[cliente.nit] = cliente
    def guardar_datos(self):
        with open(self.archivo_nombre, "w", encoding = 'utf-8') as f:
            for clie
class Menu:
    def __init__(self, categoria_service, producto_service, clientes_service, proveedor_service, empleado_service,
                 venta_service, compra_service):
        self.categoria_service = categoria_service
        self.producto_service = producto_service
        self.clientes_service = clientes_service
        self.proveedor_service = proveedor_service
        self.empleado_service = empleado_service
        self.venta_service = venta_service
        self.compra_service = compra_service
        self.repo_ordenamiento = Ordenamiento()

    def agregar_un_cliente(self):
        try:
            nit = input("Ingrese el Nit del cliente: ").strip()
            nombre = input("Ingrese el nombre del cliente: ").strip()
            direccion = input("Ingrese la direccion del cliente: ").strip()
            telefono = input("Ingrese el telefono del cliente: ").strip()
            correo = input("Ingrese la correo del cliente: ").strip()
            cliente = Clientes(nit, nombre, direccion, telefono, correo)
            self.clientes_service.agregar_cliente(cliente)
            print("Cliente agregado con éxito.")
            return cliente
        except ValueError:
            print("Verifica lo ingresado. No se pudo agregar el cliente.")
            return None

    def agregar_clientes(self):
        cantidad = int(input("Ingrese la cantidad de clientes: "))
        for i in range(cantidad):
            print(f"Cliente {i + 1}")
            self.agregar_un_cliente()

    def agregar_empleado(self):
        cantidad = int(input("Ingrese la cantidad de empleados: "))
        for i in range(cantidad):
            try:
                print(f"Empleado{i + 1}")
                id_empleado = input("Ingrese el Id del empleado: ").strip()
                nombre = input("Ingrese el nombre del empleado: ").strip()
                direccion = input("Ingrese la direccion del empleado: ").strip()
                telefono = input("Ingrese el telefono del empleado: ").strip()
                correo = input("Ingrese la correo del empleado: ").strip()
                puesto = input("Ingrese el puesto del empleado: ").strip()
                empleado = Empleados(id_empleado, nombre, direccion, telefono, correo, puesto)
                self.empleado_service.agregar_empleado(empleado)
                print("Empleado agregado")
            except ValueError:
                print("Verifica lo ingresado")

    def agregar_proveedor(self):
        cantidad = int(input("Ingrese la cantidad de proveedores: "))
        for i in range(cantidad):
            try:
                print(f"Proveedor {i + 1}")
                niti = input("Ingrese el NIT del proveedor: ").strip()
                nombre = input("Ingrese el nombre del proveedor: ").strip()
                direccion = input("Ingrese la direccion del proveedor: ").strip()
                telefono = input("Ingrese el telefono del proveedor: ").strip()
                correo = input("Ingrese el correo del proveedor: ").strip()
                empresa = input("Ingrese el nombre de la empresa: ").strip()

                proveedor = Proveedores(niti, nombre, direccion, telefono, correo, empresa)
                self.proveedor_service.agregar_proveedor(proveedor)
                print("Proveedor agregado con éxito.")
            except ValueError:
                print("Verifique lo ingresado.")

    def agregar_productoacomprar(self):
        idcompras = input("Ingrese el Id de la compra: ").strip()
        self.compra_service.agregar_producto_a_compra(idcompras)

    def iniciar_nuevascompras(self):
        self.compra_service.iniciar_compra()

    def listar_compras(self):
        compras = self.compra_service.repo_compras.listar()
        if not compras:
            print("No existen compras.")
            return
        print("\nListado de compras:")
        for compra in compras:
            print(compra.mostrar_compras())
            detalles_compra = [d for d in self.compra_service.repo_detallecompras.listar() if
                               d.idcompras == compra.idcompras]
            if detalles_compra:
                print("Detalles:")
                for detalle in detalles_compra:
                    print(detalle.mostrar_detallecompra())

    def listar_ventas(self):
        ventas = self.venta_service.repo_venta.listar()
        if not ventas:
            print("No existen ventas")
            return
        print("\nListado de ventas")
        for venta in ventas:
            print(venta.mostrar_ventas())
            detalles_venta = [d for d in self.venta_service.repo_detalleventa.listar() if d.idventa == venta.idventas]
            if detalles_venta:
                print("Detalles:")
                for detalle in detalles_venta:
                    print(detalle.mostrar_detalleventas())

    def agregar_productoaventa(self):
        idventa = input("Ingrese el Id de la venta").strip()
        self.venta_service.agregar_productoaventa(idventa)

    def nueva_venta(self):
        self.venta_service.iniciar_venta()

    def agregar_categoria(self):
        canti = int(input("Ingrese la cantidad de categorias: "))
        for i in range(canti):
            try:
                print(f"Categoria {i + 1}")
                idcat = input("Ingrese Id de categoria: ").strip()
                nomcat = input("Ingrese Nombre de categoria: ").strip()
                categoria = Categoria(idcat, nomcat)
                self.categoria_service.agregar_categoria(categoria)
                print("Agregado")
            except ValueError:
                print("Verifica lo ingresado")

    def listar_categorias(self):
        categorias = self.categoria_service.listar()
        if not categorias:
            print("No hay categorias")
            return
        for c in categorias:
            print(c.mostrar_categoria())

    def agregar_productos(self):
        if not self.categoria_service.listar():
            print("\nprimero debes agregar una categoria")
            return
        cantidad = int(input("Ingrese la cantidad de productos: "))
        for i in range(cantidad):
            try:
                print(f"Producto {i + 1}")
                while True:
                    codigo = input("Ingrese la codigo del producto: ").strip()
                    if self.producto_service.obtener_producto(codigo):
                        print("El codigo ya existe")
                    else:
                        break
                nombre = input("Ingrese el nombre del producto: ").strip()
                print("Categorias Disponibles")
                self.listar_categorias()
                id_categoria = input("Ingrese la id del categoria: ").strip()
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto: "))
                producto = Productos(codigo, nombre, precio, id_categoria, stock)
                self.producto_service.agregar_producto(producto)
            except ValueError:
                print("Verifica lo ingresado")

    def listar_producto(self):
        productos = self.producto_service.listar()
        if not productos:
            print("No hay productos")
            return
        for i in productos:
            print(i.mostrar_producto())

    def listar_productos_ordenados(self):
        print("Ordenar por: 1.Nombre, 2.Precio, 3.Stock")
        op = int(input("Ingrese la opcion: ").strip())
        match op:
            case 1:
                productos = self.repo_ordenamiento.por_nombre(self.producto_service.listar())
            case 2:
                productos = self.repo_ordenamiento.por_precio(self.producto_service.listar())
            case 3:
                productos = self.repo_ordenamiento.por_stock(self.producto_service.listar())
            case _:
                print("opción invalida")
                return
        for i in productos:
            print(i.mostrar_producto())

    def actualizar_producto(self):
        self.producto_service.listar()
        codigo = input("Ingrese la codigo del producto: ").strip()
        producto = self.producto_service.obtener_producto(codigo)
        if not producto:
            print("no existe")
            return
        try:
            print(f"producto actual:"
                  f"{producto.mostrar_producto()}")
            nuevo_precio_str = input("Ingrese el nuevo precio del producto(enter si no): ")
            nuevo_stock_str = input("Ingrese el nuevo stock(enter si no)")
            nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None
            nuevo_stock = int(nuevo_stock_str) if nuevo_stock_str else None
            self.producto_service.actualizar_producto(
                idproducto=codigo, nuevo_precio=nuevo_precio, nuevo_stock=nuevo_stock)
        except ValueError:
            print("Verifica lo ingresado")

    def eliminar_producto(self):
        codigo = input("Ingrese la codigo del producto: ").strip()
        self.producto_service.eliminar_producto(codigo)

    def gestionar_venta(self):
        self.venta_service.gestionar_venta_completa()

    def mostrar_menu(self):
        while True:
            print("\nMenu principal")
            print("1.Listado Categoria")
            print("2.Agregar Categoria")
            print("3.Agregar Productos")
            print("4.agregar cliente")
            print("5.agregar empleado")
            print("6.agregar proveedor")
            print("7.Listar Productos Ordenados")
            print("8.Actualizar producto")
            print("9.Eliminar producto")
            print("10.Gestionar Venta (Iniciar y agregar productos)")
            print("11.lista ventas")
            print("12.nueva compra")
            print("13.agregar producto a comprar")
            print("14.listar compras")
            print("15. Salir")
            try:
                op = int(input("Ingrese una opción: "))
                match op:
                    case 1:
                        self.listar_categorias()
                    case 2:
                        self.agregar_categoria()
                    case 3:
                        self.agregar_productos()
                    case 4:
                        self.agregar_clientes()
                    case 5:
                        self.agregar_empleado()
                    case 6:
                        self.agregar_proveedor()
                    case 7:
                        self.listar_productos_ordenados()
                    case 8:
                        self.actualizar_producto()
                    case 9:
                        self.eliminar_producto()
                    case 10:
                        self.gestionar_venta()
                    case 11:
                        self.listar_ventas()
                    case 12:
                        self.iniciar_nuevascompras()
                    case 13:
                        self.agregar_productoacomprar()
                    case 14:
                        self.listar_compras()
                    case 15:
                        print("Hasta que nos volvamos a ver")
                        break
            except ValueError:
                print("Verifica lo ingresado")
if __name__ == "__main__":
    # Repositorios
    repo_categorias = RepositorioCategoriasMemoria()
    repo_productos = RepositorioProductosMemoria()
    repo_clientes = RepositorioClientesMemoria()
    repo_proveedor = RepositorioProveedoresMemoria()
    repo_empleado = RepositorioEmpleadosMemoria()
    repo_venta = RepositorioVentasMemoria()
    repo_detalleventa = RepositorioDetalleVentaMemoria()
    repo_compra = RepositorioComprasMemoria()
    repo_detallecompra = RepositorioDetalleComprasMemoria()
    # Servicios
    categoria_service = CategoriaService(repo_categorias)
    producto_service = ProductoService(repo_productos, repo_categorias)
    clientes_service = ClientesService(repo_clientes)
    proveedor_service = ProveedorService(repo_proveedor)
    empleado_service = EmpleadoService(repo_empleado)
    venta_service = VentaService(repo_venta, repo_detalleventa, clientes_service, empleado_service, producto_service)
    compra_service = CompraService(repo_compra, repo_detallecompra, proveedor_service, producto_service)
    # Menú principal (pasando los servicios al menú)
    menu = Menu(categoria_service, producto_service, clientes_service, proveedor_service, empleado_service,
                venta_service, compra_service)
    menu.mostrar_menu()