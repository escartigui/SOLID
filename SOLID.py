from abc import ABC, abstractmethod
class Categoria:
    def __init__(self, idcategoria, nombre):
        self.idcategoria = idcategoria
        self.nombre = nombre
    def mostrar_categoria(self):
        return f"Categoria:{self.idcategoria} Nombre:{self.nombre}"
class Productos:
    def __init__(self, idproducto, nombre,precio,idcategoria,stock = 0):
        self.idproducto = idproducto
        self.nombre = nombre
        self.precio = precio
        self.idcategoria = idcategoria
        self.stock = stock
    def mostrar_producto(self):
        return f"Producto; Codigo: {self.idproducto},Nombre: {self.nombre},Precio: {self.precio},IdCategoria: {self.idcategoria},Stock: {self.stock}"
class Clientes:
    def __init__(self,nit,nombre,direccion,telefono, correo):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def mostrar_clientes(self):
        return f"Clientes: {self.nit}, {self.nombre}, {self.direccion}, {self.telefono}, {self.correo}"
class Proveedores:
    def __init__(self, nit, nombre,direccion, telefono, correo, empresa):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.empresa = empresa

    def mostrar_proveedores(self):
        return f"Proveedores: {self.nit}, {self.nombre}, {self.direccion}, {self.telefono}, {self.correo}"
class Empleados:
    def __init__(self,idempleado, nombre,direccion,telefono,correo,puesto):
        self.Id_Empleado = idempleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto

    def mostrar_empleados(self):
        return f"Empleado(s): {self.Id_Empleado}, {self.nombre}, {self.direccion}, {self.telefono}, {self.correo}, {self.puesto}"
class IRepositorioCategorias(ABC):
    @abstractmethod
    def agregar(self,categoria):
        pass
    @abstractmethod
    def listar(self):
        pass
    @abstractmethod
    def obtener(self,idcategoria):
        pass
class IRepositorioProductos(ABC):
    @abstractmethod
    def agregar(self,producto):
        pass
    @abstractmethod
    def listar(self):
        pass
    def obtener(self,idproducto):
        pass
    def eliminar(self,idproducto):
        pass
class IRepositorioClientes(ABC):
    @abstractmethod
    def agregar(self,cliente):
        pass
    def listar(self):
        pass
    def obtener(self,nit):
        pass
class RepositorioClientesMemoria(IRepositorioClientes):
    def __init__(self):
        self.clientes = {}
    def agregar(self,cliente):
        self.clientes[cliente.nit]=cliente
    def listar(self):
        return list(self.clientes.values())
    def obtener(self,nit):
        return self.clientes.get(nit)
class RepositorioCategoriasMemoria(IRepositorioCategorias):
    def __init__(self):
        self.categorias = {}
    def agregar(self,categoria):
        self.categorias[categoria.idcategoria] = categoria
    def listar(self):
        return list(self.categorias.values())
    def obtener(self,idcategoria):
        return self.categorias.get(idcategoria)
class RepositorioProductosMemoria(IRepositorioProductos):
    def __init__(self):
        self.productos = {}
    def agregar(self,producto):
        self.productos[producto.idproducto] = producto
    def listar(self):
        return list(self.productos.values())
    def obtener(self,idproducto):
        return self.productos.get(idproducto)
    def eliminar(self,idproducto):
        if idproducto in self.productos:
            del self.productos[idproducto]
            print("Productos eliminado")
        else:
            print("producto no encontrado")
class ClientesService:
    def __init__(self, repo_clientes):
        self.repo_clientes = repo_clientes
    def agregar_cliente(self,cliente):
        self.repo_clientes.agregar(cliente)
    def listar(self):
        return self.repo_clientes.listar()
class CategoriaService:
    def __init__(self, repo_categoria):
        self.repo_categorias = repo_categoria
    def agregar_categoria(self,categoria):
        if any(c.nombre == categoria.nombre for c in self.repo_categorias.listar()):
            print("Ya existe")
            return
        self.repo_categorias.agregar(categoria)
    def listar(self):
        return self.repo_categorias.listar()
class ProductoService:
    def __init__(self, repo_producto,repo_categoria):
        self.repo_producto = repo_producto
        self.repo_categoria = repo_categoria
    def agregar_producto(self,producto):
        if not self.repo_categoria.obtener(producto.idcategoria):
            print("Primero la categoria")
            return
        self.repo_producto.agregar(producto)
        print("Producto agregado")
    def listar(self):
        return self.repo_producto.listar()
    def obtener_producto(self,idproducto):
        return self.repo_producto.obtener(idproducto)
    def eliminar_producto(self,idproducto):
        producto = self.repo_producto.obtener(idproducto)
        if producto:
            self.repo_producto.eliminar(idproducto)
        else:
            print("producto no encontrado")
    def actualizar_producto(self,idproducto,nuevo_precio = None,nuevo_stock = None):
        producto = self.repo_producto.obtener(idproducto)
        if not producto:
            print("producto no encontrado")
            return
        if nuevo_precio is not None:
            producto.precio = nuevo_precio
        if nuevo_stock is not None:
            producto.stock = nuevo_stock
        print("Editado correctamente")
class Ordenamiento:
    @staticmethod
    def por_nombre(productos):
        def funcion_nom(producto):
            return producto.nombre.lower()
        return sorted(productos,key = funcion_nom)
    @staticmethod
    def por_precio(productos):
        def funcion_precio(producto):
            return producto.precio
        return sorted(productos,key = funcion_precio)
    @staticmethod
    def por_stock(productos):
        def funcion_stock(producto):
            return producto.stock
        return sorted(productos,key = funcion_stock)
class Menu:
    def __init__(self,categoria_service,producto_service,clientes_service):
        self.categoria_service = categoria_service
        self.producto_service = producto_service
        self.clientes_service = clientes_service
        self.repo_ordenamiento = Ordenamiento()

    def agregar_categoria(self):
        canti = int(input("Ingrese la cantidad de categorias: "))
        for i in range(canti):
            try:
                print(f"Categoria {i+1}")
                idcat = input("Ingrese Id de categoria: ").strip()
                nomcat = input("Ingrese Nombre de categoria: ").strip()
                categoria = Categoria(idcat,nomcat)
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
                print(f"Producto {i+1}")
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
                producto = Productos(codigo,nombre,precio,id_categoria,stock)
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
            nuevo_precio = float (nuevo_precio_str) if nuevo_precio_str else None
            nuevo_stock = int(nuevo_stock_str) if nuevo_stock_str else None
            self.producto_service.actualizar_producto(
                idproducto = codigo,nuevo_precio=nuevo_precio, nuevo_stock=nuevo_stock)
        except ValueError:
            print("Verifica lo ingresado")
    def eliminar_producto(self):
        codigo = input("Ingrese la codigo del producto: ").strip()
        self.producto_service.eliminar_producto(codigo)
    def mostrar_menu(self):
        while True:
            print("\nMenu principal")
            print("1.Listado Categoria")
            print("2.Agregar Categoria")
            print("3.Agregar Productos")
            print("4.Listar Productos Ordenados")
            print("5.Actualizar")
            print("6.Eliminar")
            print("7.Salir")
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
                        self.listar_productos_ordenados()
                    case 5:
                        self.actualizar_producto()
                    case 6:
                        self.eliminar_producto()
                    case 7:
                        print("Hasta que nos volvamos a ver")
                        break
            except ValueError:
                print("Verifica lo ingresado")
if __name__ == "__main__":
    # Repositorios
    repo_categorias = RepositorioCategoriasMemoria()
    repo_productos = RepositorioProductosMemoria()
    repo_clientes = RepositorioClientesMemoria()

    # Servicios
    categoria_service = CategoriaService(repo_categorias)
    producto_service = ProductoService(repo_productos, repo_categorias)
    clientes_service = ClientesService(repo_clientes)

    # Menú principal (pasando los servicios al menú)
    menu = Menu(categoria_service, producto_service,clientes_service)
    menu.mostrar_menu()