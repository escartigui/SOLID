class Categoria:
    def __init__(self, Id_categoria, nombre):
        self.Id_categoria = Id_categoria
        self.nombre = nombre

    def mostrarcategoria(self):
        return f"Categoria: {self.Id_categoria} {self.nombre}"

class Productos:
    def __init__(self, codigo, nombre, precio,Id_producto, totalcompra, totalventa,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.Id_producto = Id_producto
        self.totalcompra = totalcompra
        self.totalventa = totalventa
        self.stock = stock

    def mostrar_productos(self):
        return f"productos: {self.codigo}, {self.nombre}, {self.precio}, {self.totalcompra}, {self.totalventa}, {self.stock}"

class Manipulacion_Categoria:
    def __init__(self):
        self.categorias = {}

    def agregar(self):
        try:
            cantidad = int(input("Ingrese la cantidad de categorias: "))
            for i in range(cantidad):
                print(f"categoria{i+1}")
                Id_categoria = input("Ingrese la codigo de categoria:").lower()
                if Id_categoria.lower() in self.categoria:
                    print("el codigo ya existe")
                    return
                if Id_categoria == "":
                    print("el codigo no puede quedar vacio")
                    return
                nombre = input("Ingrese la categoria: ")
                if nombre == "":
                    print("No puede quedar vacio")
                    return
                self.categorias[Id_categoria] = Categoria(Id_categoria, nombre)
        except ValueError:
            print("Verifica lo ingresado")
