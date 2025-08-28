class Categoria:
    def __init__(self, idcategoria, nombre):
        self.Id_categoria = idcategoria
        self.nombre = nombre

    def mostrarcategoria(self):
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

    def mostrar_productos(self):
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

    def agregar(self):
        try:
            cantidad = int(input("Ingrese la cantidad de categorias: "))
            for i in range(cantidad):
                print(f"categoria{i+1}")
                idcategoria = input("Ingrese la codigo de categoria:").lower()
                if idcategoria.lower() in self.categorias:
                    print("el codigo ya existe")
                    return
                if idcategoria.strip() == "":
                    print("el codigo no puede quedar vacio")
                    return
                nombre = input("Ingrese la categoria: ")
                if nombre == "":
                    print("No puede quedar vacio")
                    return
                self.categorias[idcategoria] = Categoria(idcategoria, nombre)
        except ValueError:
            print("Verifica lo ingresado")
class ManipulacionProducto:
    def __init__(self):
        self.productos = {}

    def agregar(self):
        try:
            cantidad = int(input("Ingrese la cantidad de productos: "))
            for i in range(cantidad):
                print(f"producto{i+1}")
                codigo = input("Ingrese la codigo de producto: ").lower()
                if codigo.lower() in self.productos:
                    print("El codigo ya existe")
                    return
                if codigo.strip() == "":
                    print("El codigo no puede quedar vacio")
                    return
                nombre = input("Ingrese el nombre del producto")
                if nombre.strip() == "":
                    print("No puede quedar vacio")
                idcategoria = input("Ingrese la codigo de categoria: ").lower()
                if idcategoria not in Categoria:
                    print("Error: La categoria no existe. agrega una categoria")
                else:
                    precio = float(input("Ingrese el precio del producto: "))
                    if precio < 0:
                        print("El precio no puede ser negativo")
                        return
                    if precio == "":
                        print("No puede quedar vacio")
                        return
                    totalcompra = float(input("Ingrese el total de compra: "))
                    if totalcompra < 0:
                        print("El total no puede ser negativo")
                        return
                    if totalcompra == "":
                        print("No puede quedar vacio")
                        return
                    totalventa = float(input("Ingrese el total de venta: "))
                    if totalventa < 0:
                        print("El total no puede ser negativo")
                        return
                    if totalventa == "":
                        print("No puede quedar vacio")
                        return
                    stock = input("Ingrese el stock: ")
                    if stock.strip() == "":
                        print("No puede quedar vacio")
                        return
        except ValueError:
            print("Verifica lo ingresado")
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
            except ValueError:
                print("Verifica lo ingresado")