# Entradas

base = float(input("Ingrese el valor de la base:"))
altura = float(input("Ingrese el valor de la altura:"))

# Proceso

def calcularAreaTriangulo(b,al):
    area = (b*al)/2
    return area

# salida

resultado = calcularAreaTriangulo(base, altura)
print("El area del triangulo es: ", resultado)


# Funcion con argumentos por defecto

def mostrarPais(pais = "Colombia"):
    print("Yo soy de:" + " "+pais)

mostrarPais("Suiza")
mostrarPais("Ecuador")
mostrarPais()
mostrarPais("Brazil")