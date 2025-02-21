#INVENTARIO
inventario = {"manzanas": 430, "bananas": 312, "naranjas": 525, "peras": 217}

#BUCLE PRINCIPAL (WHILE TRUE)

while True:
    input_accion = input("Elige una acción (escribe 'ver' para ver el inventario, 'comprar' para comprar una fruta, 'salir' para salir): ").lower()

    if input_accion == "ver":
        print("\nInventario actual:")
        for fruta, cantidad in inventario.items():  # Usando el iterador
            print(f"- {fruta.capitalize()}: {cantidad} unidades")
        print()  # Salto de línea

    elif input_accion == "comprar":
        fruta = input("¿Qué fruta quieres comprar? ").lower()
        inventario_lower = {k.lower(): v for k, v in inventario.items()}  # Convertir a minúsculas

        if fruta in inventario_lower:
            try:
                cantidad = int(input(f"¿Cuántas unidades de {fruta} quieres comprar? "))
                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor que 0.")
                elif cantidad > inventario_lower[fruta]:
                    print("⚠️ No hay suficiente stock.")
                else:
                    inventario[fruta] -= cantidad
                    print(f"✅ Compra exitosa. Ahora quedan {inventario[fruta]} unidades de {fruta}.")
            except ValueError:
                print("⚠️ Por favor, introduce un número entero válido.")
        else:
            print("⚠️ Esa fruta no está en el inventario.")

    elif input_accion == "salir":
        print("¡Gracias por usar el sistema! ¡Hasta luego! 👋")
        break

    else:
        print("⚠️ Acción no válida. Por favor, elige 'ver', 'comprar' o 'salir'.")

#ITERADOR
iterador = iter(inventario.items())
print(next(iterador))
print(next(iterador))
print(next(iterador))   
#FIN

#CLASE
class inventario:
    def __init__(self, inventario):
        self.inventario = inventario
        self.iterador = iter(inventario.items())

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return next(self.iterador)
        except StopIteration:
            raise StopIteration("No hay más elementos en el inventario.")
        
mi_inventario = inventario(inventario)

for fruta, cantidad in mi_inventario:
    print(f"{fruta.capitalize()}: {cantidad} unidades")
#FIN
    