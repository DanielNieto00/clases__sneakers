# -------------------------
# CLASES
# -------------------------

class Usuario:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_info(self):
        return f"{self.nombre} - {self.email}"


class Producto:
    def __init__(self, id, nombre, marca, talla, precio, stock):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.talla = talla
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"{self.id}. {self.nombre} ({self.marca}) - Talla {self.talla} - ${self.precio}"

    def reducir_stock(self):
        self.stock -= 1


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto.stock > 0:
            self.productos.append(producto)
            producto.reducir_stock()
            print("✅ Producto agregado")
        else:
            print("❌ Sin stock")

    def mostrar_carrito(self):
        print("\n🛒 Carrito:")
        for p in self.productos:
            print(p.mostrar_info())

    def calcular_total(self):
        return sum(p.precio for p in self.productos)


class Pedido:
    def __init__(self, usuario, productos):
        self.usuario = usuario
        self.productos = productos
        self.total = sum(p.precio for p in productos)
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmado"

    def mostrar_resumen(self):
        print("\n📦 Pedido:")
        for p in self.productos:
            print(p.mostrar_info())
        print(f"Total: ${self.total}")


class Pago:
    def __init__(self, metodo, monto):
        self.metodo = metodo
        self.monto = monto

    def procesar(self):
        print(f"💳 Pago realizado con {self.metodo} por ${self.monto}")


class Envio:
    def __init__(self, direccion, tipo):
        self.direccion = direccion
        self.tipo = tipo

    def calcular_costo(self):
        if self.tipo == "express":
            return 20000
        return 10000


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("\n👟 Productos disponibles:")
        for p in self.productos:
            print(p.mostrar_info())


# -------------------------
# MAIN (SIMULACIÓN)
# -------------------------

tienda = Tienda()

# Productos
p1 = Producto(1, "Air Jordan 1", "Nike", 42, 500000, 5)
p2 = Producto(2, "Yeezy 350", "Adidas", 41, 700000, 3)

tienda.agregar_producto(p1)
tienda.agregar_producto(p2)

# Usuario
usuario = Usuario("Daniel", "nietodaniel365@gmail.com", "Barranquilla", "123456")

# Carrito
carrito = Carrito()

while True:
    print("\n--- MENÚ ---")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Ver carrito")
    print("4. Comprar")
    print("5. Salir")

    opcion = input("Elige: ")

    if opcion == "1":
        tienda.mostrar_productos()

    elif opcion == "2":
        id_producto = int(input("ID del producto: "))
        for p in tienda.productos:
            if p.id == id_producto:
                carrito.agregar_producto(p)

    elif opcion == "3":
        carrito.mostrar_carrito()

    elif opcion == "4":
        pedido = Pedido(usuario, carrito.productos)
        pedido.confirmar()
        pedido.mostrar_resumen()

        pago = Pago("Tarjeta", pedido.total)
        pago.procesar()

        envio = Envio(usuario.direccion, "express")
        costo = envio.calcular_costo()

        print("🚚 Costo envío:", costo)
        print("💰 Total final:", pedido.total + costo)

    elif opcion == "5":
        print("👋 Saliendo...")
        break
