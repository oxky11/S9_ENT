def sumar(a, b):
 if puedeSerCalculado(a, b):
  return a + b
 else:
  return "Error al calcular. Uno de los elementos no es un número"

def restar(a, b):
 if puedeSerCalculado(a, b):
  return a - b
 else:
  return "Error al calcular. Uno de los elementos no es un número"

def multiplicar(a, b):
 if puedeSerCalculado(a, b):
  return a * b
 else:
  return "Error al calcular. Uno de los elementos no es un número"

def dividir(a, b):
 if puedeSerCalculado(a, b):
  return a / b
 else:
  return "Error al calcular. Uno de los elementos no es un número"


# Implementation of isNumber() function
def puedeSerCalculado(a, b):

# try to convert the string to int
 try:
  n = int(a)
  n = int(b)
  return True
 # catch exception if cannot be converted
 except ValueError:
  return False


if __name__ == "__main__":
 print(sumar(5, 'a'))
 print(restar(5, -6))
 print(multiplicar(5, 4))
 print(dividir(6, 3))