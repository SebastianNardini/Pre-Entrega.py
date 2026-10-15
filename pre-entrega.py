productos = []
print("*"*25)
print(f" Sistema de gestion de productos")
print(f" \t                   MENU")
print("*"*25)

# Crear función para agregar producto
def agregar_producto():
    while True:
        nombre = input(f"Nombre del producto (o 5 para salir): ").strip().title()
        if nombre == "5":
            print (f"Gracias por usar el sistema")
            break
        while nombre == "":
            print(f"Completa con un nombre valido.")
            nombre = input(f"Nombre del producto: ").strip().title()

        categoria = input(f"Nombre la categoria: ").strip().title()
        if categoria == "5":
            print (f"Gracias por usar el sistema")
            break
        while categoria == "":
            print(f"La categoria no puede estar vacia.")
            categoria = input(f"Nombre la categoria: ").strip().title()

        precio_str = input (f"Precio $ (sin centavos): ")
        if precio_str == "5":
            print (f"Gracias por usar el sistema")
            break
        while precio_str == "" or not precio_str.isdigit():
            if precio_str == "":
                print(f"El precio no puede estar vacio.")
            else:
                print (f"Ingresar precio sin centavos")
            precio_str = input (f"Precio $ (sin centavos): ")
        precio = int(precio_str)
        
        productor_ingresado = [nombre, categoria, precio]
        productos.append(productor_ingresado)
        print ("Producto agregado correctamente.")
        break

def mostrar_producto():
    print (f"Seleccionaste la opcion 2: Mostrar productos")
    if len(productos) == 0:
        print (f"No hay productos ingresados")
    else:
        print (f"Productos agregados: ")
        for indice, producto in enumerate(productos, 1):
            print(f"{indice}. Nombre: {producto[0]}, Categoria: {producto[1]}, Precio: $ {producto[2]} ")

def buscar_producto():
    print (f"Seleccionaste la opcion 3: Buscar producto")
    if len(productos) == 0:
        print (f"No hay productos ingresados")
    else:
        producto_buscado = input (f"Ingresa el producto buscado: ").strip().lower()
        while producto_buscado == "":
            print (f"El nombre del producto no puede estar vacio")
            producto_buscado = input (f"Ingresa el producto buscado: ").strip().lower()
        
        encontrado = False
        for producto in productos:
            if producto_buscado in producto[0].lower():
                print (f"Producto encontrado: Nombre: {producto[0]}, Categoria: {producto[1]}, Precio: $ {producto[2]}")
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

def eliminar_producto():
    print (f"Seleccionaste la opcion 4: Eliminar producto")
    if len(productos) == 0:
        print (f"No hay productos ingresados")
    else:
        for i in range(len(productos)):
            print(f"{i+1}. Nombre: {productos[i][0]}, Categoria: {productos[i][1]}, Precio: $ {productos[i][2]}")
        
        producto_eliminar = input(f"Ingresa el numero del producto a eliminar: ").strip()
        while not producto_eliminar.isdigit() or int(producto_eliminar) < 1 or int(producto_eliminar) > len(productos):
            print(f"Selecciona un numero valido de producto a eliminar.")
            producto_eliminar = input(f"Ingresa el numero del producto a eliminar: ").strip()
            
        eliminado = productos.pop(int(producto_eliminar) - 1)
        print(f"Producto eliminado: Nombre: {eliminado[0]}, Categoria: {eliminado[1]}, Precio: $ {eliminado[2]}")

def menu():
    while True:
        print("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir")
        opcion = input(f"Selecciona una opcion (1-5): ").strip()
        while opcion == "":
            print(f"Opcion no valida.")
            opcion = input(f"Selecciona una opcion (1-5): ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print (f"Gracias por usar el sistema")
            break
        else:
            print (f"Opcion no valida")

menu()