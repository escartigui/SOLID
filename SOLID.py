class Categoria:
    def __init__(self, idcategoria, nombre):
        self.Id_categoria = idcategoria
        self.nombre = nombre

    def mostrar_categoria(self):
        return f"Categoria: {self.Id_categoria} {self.nombre}"
class Productos:
    def __init__(self, codigo, nombre,idproducto,precio, totalcompra, totalventa,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.Id_producto = idproducto
        self.precio = precio
        self.totalcompra = totalcompra
        self.totalventa = totalventa
        self.stock = stock

    def mostrar_producto(self):
        return f"productos: {self.codigo}, {self.nombre}, {self.precio}, {self.totalcompra}, {self.totalventa}, {self.stock}"
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
class ManipulacionCategoria:
    def __init__(self):
        self.categorias = {}

    def agregar(self,categoria:Categoria):
            if categoria.Id_categoria.lower() in self.categorias:
                raise ValueError("El Id ya existe")
            self.categorias[categoria.Id_categoria] = categoria
    def obtener(self,id_categoria):
            return self.categorias.get(id_categoria)
    def listar(self):
            return list(self.categorias.values())
class ManipulacionProducto:
    def __init__(self):
        self.productos = {}

    def agregar(self,producto:Productos):
        if producto.codigo.lower() in self.productos:
            raise ValueError("El codigo ya existe")
        self.productos[producto.codigo] = producto

    def obtener(self, codigo):
        return self.productos.get(codigo)

    def eliminar(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]

    def listar(self):
        return list(self.productos.values())
class Ordenamiento:
    def por_nombre(self,productos):
        def funcion_nom(producto):
            return producto.nombre.lower()
        return sorted(productos,key = funcion_nom)

    def por_precio(self,productos):
        def funcion_precio(producto):
            return producto.precio
        return sorted(productos,key = funcion_precio)

    def por_stock(self,productos):
        def funcion_stock(producto):
            return producto.stock
        return sorted(productos,key = funcion_stock)
registroprod = ManipulacionProducto()
class Manipulacionclientes:
    def __init__(self):
        self.clientes = {}

    def agregar(self):
        try:
            cantidad = int(input("Ingrese la cantidad de clientes: "))
            for i in range(cantidad):
                print(f"Clientes{i+1}")
                nit = input("Ingrese el nit del cliente: ").lower()
                if nit.lower() in self.clientes:
                    print("El nit ya existe")
                    return
                if nit.strip() == "":
                    print("El nit no puede quedar vacio")
                    return
                nombre = input("Ingrese el nombre del producto")
                if nombre.strip() == "":
                    print("No puede quedar vacio")
                    return
                direccion = input("Ingrese la direccion del cliente: ")
                if direccion.strip() == "":
                    print("No puede quedar vacio")
                    return
                telefono = int(input("Ingrese el numero de telefono del cliente: "))
                if telefono == "":
                    print("No puede quedar vacio")
                    return
                correo = input("Ingrese la correo del cliente: ")
                if correo.strip() == "":
                    print("No puede quedar vacio")
                    return
                self.clientes[nit] = Clientes(nit,nombre, direccion, telefono, correo)
        except ValueError:
            print("Verifica lo ingresado")
class ManipulacionProveedores:
    def __init__(self):
        self.proveedores = {}

    def agregar(self):
        try:
            cantidad = int(input("Ingrese la cantidad de productos: "))
            for i in range(cantidad):
                print(f"Clientes{i+1}")
                nit = input("Ingrese el nit del cliente: ").lower()
                if nit.lower() in self.proveedores:
                    print("El nit ya existe")
                    return
                if nit.strip() == "":
                    print("El nit no puede quedar vacio")
                    return
                nombre = input("Ingrese el nombre del producto")
                if nombre.strip() == "":
                    print("No puede quedar vacio")
                    return
                direccion = input("Ingrese la direccion del cliente: ")
                if direccion.strip() == "":
                    print("No puede quedar vacio")
                    return
                telefono = int(input("Ingrese el numero de telefono del cliente: "))
                if telefono == "":
                    print("No puede quedar vacio")
                    return
                correo = input("Ingrese la correo del cliente: ")
                if correo.strip() == "":
                    print("No puede quedar vacio")
                    return
                empresa = input("Ingrese el nombre de la empresa: ")
                if empresa.strip() == "":
                    print("No puede quedar vacio")
                    return
                self.proveedores[nit] = Proveedores(nit,nombre, direccion, telefono, correo,empresa)
        except ValueError:
            print("Verifica lo ingresado")
class ManipulacionEmpleados:
    def __init__(self):
            self.empleados = {}

    def agregar(self):
            try:
                cantidad = int(input("Ingrese la cantidad de empleados: "))
                for i in range(cantidad):
                    print(f"Clientes{i + 1}")
                    idempleado = input("Ingrese el id del empleado: ").lower()
                    if idempleado.lower() in self.empleados:
                        print("El nit ya existe")
                        return
                    if idempleado.strip() == "":
                        print("El nit no puede quedar vacio")
                        return
                    nombre = input("Ingrese el nombre del producto")
                    if nombre.strip() == "":
                        print("No puede quedar vacio")
                        return
                    direccion = input("Ingrese la direccion del cliente: ")
                    if direccion.strip() == "":
                        print("No puede quedar vacio")
                        return
                    telefono = int(input("Ingrese el numero de telefono del cliente: "))
                    if telefono == "":
                        print("No puede quedar vacio")
                        return
                    correo = input("Ingrese la correo del cliente: ")
                    if correo.strip() == "":
                        print("No puede quedar vacio")
                        return
                    puesto = input("Ingrese el puesto: ")
                    if puesto.strip() == "":
                        print("No puede quedar vacio")
                        return
                    self.empleados[idempleado] = Empleados(idempleado,nombre, direccion, telefono, correo,puesto)
            except ValueError:
                print("Verifica lo ingresado")
class Menu:
    def __init__(self):
        self.repo_categorias = ManipulacionCategoria()
        self.repo_productos = ManipulacionProducto()
        self.repo_ordenamiento = Ordenamiento()

    def agregar_categoria(self):
        canti = int(input("Ingrese la cantidad de categorias: "))
        for i in range(canti):
            print(f"Categoria {i+1}")
            idcat = input("Ingrese Id de categoria: ").strip()
            nomcat = input("Ingrese Nombre de categoria: ").strip()
            try:
                categoria = Categoria(idcat,nomcat)
                self.repo_categorias.agregar(categoria)
                print("Agregado")
            except ValueError:
                print("Verifica lo ingresado")

    def listar_categorias(self):
        categorias = self.repo_categorias.listar()
        if not categorias:
            print("No hay categorias")
            return
        for c in categorias:
            print(c.mostrar_categoria())

    def agregar_productos(self):
        if not self.repo_categorias.listar():
            print("Debes agregar la categoria primero")
            return
        cantidad = int(input("Ingrese la cantidad de productos: "))
        for i in range(cantidad):
            try:
                print(f"Producto {i+1}")
                codigo = input("Ingrese la codigo del producto: ").strip()
                nombre = input("Ingrese el nombre del producto: ").strip()
                print("categorias")
                self.listar_categorias()
                id_categoria = input("Ingrese la id del categoria: ").strip()
                categoria = self.repo_categorias.obtener(id_categoria)
                if not categoria:
                    print("Deberias agregarla")
                    return
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto: "))
                totalventa = int(input("Ingrese el total venta del producto: "))
                totalcompra = int(input("Ingrese el total compra del producto: "))
                producto = Productos(codigo,nombre,categoria,precio,stock,totalventa,totalcompra)
                self.repo_productos.agregar(producto)
                print("Se agrego")
            except ValueError:
                print("Verifica lo ingresado")
    def listar_producto(self):
        productos = self.repo_productos.listar()
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
                productos = self.repo_ordenamiento.por_nombre(self.repo_productos.listar())
            case 2:
                productos = self.repo_ordenamiento.por_precio(self.repo_productos.listar())
            case 3:
                productos = self.repo_ordenamiento.por_stock(self.repo_productos.listar())
            case _:
                print("opción invalida")
                return
        for i in productos:
            print(i.mostrar_producto())

    def actualizar_producto(self):
        codigo = input("Ingrese la codigo del producto: ").strip()
        producto = self.repo_productos.obtener(codigo)
        if not producto:
            print("no existe")
            return
        try:
            precio = input("ingrese el nuevo precio: ")
            stock = int(input("ingrese el stock: "))
            if precio:
                producto.precio = float(precio)
            if stock:
                producto.stock = int(stock)
            print("Listo")
        except ValueError:
            print("Verifica lo ingresado")
    def eliminar_producto(self):
        codigo = input("Ingrese la codigo del producto: ").strip()
        producto = self.repo_productos.obtener(codigo)
        if not producto:
            print("no existe")
            return
        self.repo_productos.eliminar(producto)
        print("Se eliminado")
    def mostrar_menu(self):
        while True:
            print("Menu principal")
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
                        break
            except ValueError:
                print("Verifica lo ingresado")
menu = Menu()
menu.mostrar_menu()