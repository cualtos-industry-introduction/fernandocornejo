def opciones():
    op = input("Ingresa una opción: ")
    if op == "b":
        print("Seleccionaste b")
    elif op == "c":
        print("Seleccionaste c")
    elif op in ['a', 'e', 'i', 'o', 'u']:
        print("Seleccionaste una vocal")
    else:
        print("Todo lo demás")

if __name__ == "__main__":
    variable = input("Hey boy: ")
    print(variable)
    print([x for x in range(10)])
    salir = "no"
    while(salir in ["no", "No", "NO"]):
        opciones()
        salir = input("¿Deseas salir? ")
    
    diccionario = [
        {"nombre":"Fulanito", "apellido":"Pérez"},
        {"nombre":"John", "apellido":"Doe"}
        ]
    print(diccionario)