# Nombre de la pizzería
print("Pizza la Coquette")


# Menú de pizzas
menu_pizzas = {
    "Pizza de doble queso": 800,
    "Pizza Pepperoni": 900,
    "Pizza de Hongos": 1200,
    "Pizza piña": 500
}

#  clientes de la pizzería
clientes = ["Cliente 1", "Cliente 2", "Cliente 3"]

# Facturación de cada cliente
for cliente in clientes:
    print(f"\nOrden para {cliente}:")
    orden_cliente = {}
    total_cliente = 0
    
    # Elección de pizzas
    while True:
        print("\nMenú de pizzas:")
        for pizza, precio in menu_pizzas.items():
            print(f"{pizza}: ${precio}")
        
        pizza_elegida = input("¿Qué pizza desea ordenar? (o 'fin' para terminar): ")
        
        if pizza_elegida.lower() == "fin":
            break
        
        if pizza_elegida in menu_pizzas:
            cantidad = int(input(f"Ingrese la cantidad de {pizza_elegida}: "))
            orden_cliente[pizza_elegida] = cantidad
            total_cliente += cantidad * menu_pizzas[pizza_elegida]
        else:
            print("Pizza no válida, debe elegir una del menú.")
    
    # Facturación del cliente
    print(f"\nFactura para {cliente}:")
    for pizza, cantidad in orden_cliente.items():
        print(f"{cantidad} {pizza}: ${menu_pizzas[pizza]} cada una")
    print(f"Total a pagar: ${total_cliente}")
