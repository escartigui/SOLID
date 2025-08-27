# --- ENTIDADES ---
class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def mostrar(self):
        return f"[{self.id_categoria}] {self.nombre}"


class Producto:
    def __init__(self, codigo, nombre, categoria: Categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Categoria: {self.categoria.nombre}, Precio: {self.precio}, Stock: {self.stock}"


# --- REPOSITORIOS ---
class RepositorioCategorias:
    def __init__(self):
        self.categorias = {}

    def agregar(self, categoria: Categoria):
        if categoria.id_categoria in self.categorias:
            raise ValueError("El ID de categoría ya existe")
        self.categorias[categoria.id_categoria] = categoria

    def obtener(self, id_categoria):
        return self.categorias.get(id_categoria, None)

    def listar(self):
        return list(self.categorias.values())


class RepositorioProductos:
    def __init__(self):
        self.productos = {}

    def agregar(self, producto: Producto):
        if producto.codigo in self.productos:
            raise ValueError("El código de producto ya existe")
        self.productos[producto.codigo] = producto

    def obtener(self, codigo):
        return self.productos.get(codigo, None)

    def eliminar(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]

    def listar(self):
        return list(self.productos.values())


# --- ORDENAMIENTO (sin lambda) ---
def funcion_nombre(producto):
    return producto.nombre.lower()

def funcion_precio(producto):
    return producto.precio

def funcion_stock(producto):
    return producto.stock

def ordenar_productos(productos, criterio):
    if criterio == "nombre":
        return sorted(productos, key=funcion_nombre)
    elif criterio == "precio":
        return sorted(productos, key=funcion_precio)
    elif criterio == "stock":
        return sorted(productos, key=funcion_stock)
    return productos


# --- MENÚ ---
class Menu:
    def __init__(self):
        self.repo_categorias = RepositorioCategorias()
        self.repo_productos = RepositorioProductos()

    # --- CATEGORÍAS ---
    def agregar_categoria(self):
        idc = input("ID de la categoría: ").strip()
        nombre = input("Nombre de la categoría: ").strip()
        try:
            categoria = Categoria(idc, nombre)
            self.repo_categorias.agregar(categoria)
            print("Categoría agregada.")
        except Exception as e:
            print(e)

    def listar_categorias(self):
        categorias = self.repo_categorias.listar()
        if not categorias:
            print("No hay categorías.")
            return
        for c in categorias:
            print(c.mostrar())

    # --- PRODUCTOS ---
    def agregar_producto(self):
        if not self.repo_categorias.listar():
            print("Debes agregar al menos una categoría antes de agregar productos.")
            return

        codigo = input("Código del producto: ").strip()
        nombre = input("Nombre del producto: ").strip()
        print("Categorías disponibles:")
        self.listar_categorias()
        id_categoria = input("ID de la categoría: ").strip()
        categoria = self.repo_categorias.obtener(id_categoria)
        if not categoria:
            print("Categoría no encontrada.")
            return

        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            producto = Producto(codigo, nombre, categoria, precio, stock)
            self.repo_productos.agregar(producto)
            print("Producto agregado correctamente.")
        except ValueError:
            print("Precio o stock inválido.")
        except Exception as e:
            print(e)

    def listar_productos(self):
        productos = self.repo_productos.listar()
        if not productos:
            print("No hay productos.")
            return
        for p in productos:
            print(p.mostrar())

    def listar_productos_ordenados(self):
        print("Ordenar por: 1.Nombre 2.Precio 3.Stock")
        opcion = input("Seleccione opción: ").strip()
        criterio = ""
        if opcion == "1":
            criterio = "nombre"
        elif opcion == "2":
            criterio = "precio"
        elif opcion == "3":
            criterio = "stock"
        else:
            print("Opción inválida.")
            return
        productos = ordenar_productos(self.repo_productos.listar(), criterio)
        for p in productos:
            print(p.mostrar())

    def actualizar_producto(self):
        codigo = input("Código del producto a actualizar: ").strip()
        producto = self.repo_productos.obtener(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        try:
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            stock = input("Nuevo stock (dejar vacío para no cambiar): ")
            if precio:
                producto.precio = float(precio)
            if stock:
                producto.stock = int(stock)
            print("Producto actualizado correctamente.")
        except ValueError:
            print("Precio o stock inválido.")

    def eliminar_producto(self):
        codigo = input("Código del producto a eliminar: ").strip()
        producto = self.repo_productos.obtener(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        self.repo_productos.eliminar(codigo)
        print("Producto eliminado correctamente.")

    # --- MENÚ PRINCIPAL ---
    def mostrar_menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Agregar categoría")
            print("2. Listar categorías")
            print("3. Agregar producto")
            print("4. Listar productos")
            print("5. Listar productos ordenados")
            print("6. Actualizar producto")
            print("7. Eliminar producto")
            print("8. Salir")

            opcion = input("Seleccione opción: ").strip()
            if opcion == "1":
                self.agregar_categoria()
            elif opcion == "2":
                self.listar_categorias()
            elif opcion == "3":
                self.agregar_producto()
            elif opcion == "4":
                self.listar_productos()
            elif opcion == "5":
                self.listar_productos_ordenados()
            elif opcion == "6":
                self.actualizar_producto()
            elif opcion == "7":
                self.eliminar_producto()
            elif opcion == "8":
                break
            else:
                print("Opción no válida.")


# --- EJECUCIÓN ---
menu = Menu()
menu.mostrar_menu()
