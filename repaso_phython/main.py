# tipos de datos primitivos
 # Numeros enteros

numero1: int = 57
print(numero1)

numero2 = 24
print(numero2)

# numeros reales

numero3: float = 4.9
print(numero3)

numero4 = 5.0
print(numero4)

# booleanos

esColombiano: bool = True
esArgentino = False
print(esColombiano)

# Caracter y cadena de caracteres

mensaje = "Cadena con una comilla simple ', una comilla doble \" y una diagonal invertida \\"
print(mensaje)

# Operadores
# Aritmeticos

numero5 = 9
numero6 = 12
suma = numero5 + numero6
multiplicacion = numero5 * numero6
resta = numero5 - numero6
division = numero5 / numero6
modulo = numero5 % numero6
print("La suma es: ", suma)
print("La multiplicacion es: ", multiplicacion)
print("La resta es: ", resta)
print("La division es: ", division)
print("El modulo es: ", modulo)

# Asignación

x = 7
y = 8
z = 2
print(x)

# Logicos
# and(y)
q = 5
print(q > 4 and q < 9)

# or(ó)
p = 4
print(p > 5 or p < 10)

# not
print(not(p > 2 and q < 7))

# Relacionales

valor1 = 7
valor2 = 9

print("Igualdad:", valor1 == valor2)  # Igualdad
print("Mayor que:", valor1 > valor2)   # Mayor que
print("Menor que:", valor1 < valor2)   # Menor que
print("Mayor igual que:", valor1 >= valor2) # Mayor igual que
print("Menor igual que:", valor1 <= valor2) # Menor igual que
print("No igual:", valor1 != valor2) # No igual

# Funciones
"""
las funciones son un bloque de codigo 
que solo se ejecutan cuando se llaman.
"""

def mi_funcion():
    print("¡Feliz dia!")


mi_funcion()  # Invocar la funcion

def mensaje(nombre, apellido):
    print("¡Feliz dia!"+" "+nombre+" "+apellido)


mensaje("Andrea","Rendon")


