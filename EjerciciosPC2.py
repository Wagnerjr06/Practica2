### Ejercicio 1

numeros= []
for num in range(1500,2701):
    if num % 7 == 0 and num % 5 == 0:
        numeros.append(num)
print("Los números divisibles por 7 y múltiplos de 5 entre 1500 y 2700 son ")
print (numeros)

### Ejercicio 2

n=5
for i in range(1,n+1):
    print("* " * i)
for i in range (n-1,0,-1):
    print("* " * i)

### Ejercicio 3

numeros= []
continuar= "SI"

while continuar.upper() == "SI":
    numero=int(input("Ingrese el número: "))
    numeros.append(numero)

    continuar=input("¿Desea ingresar un número? SI/NO: ").strip().upper()

pares = 0
impares= 0

for num in numeros:
    if num % 2 == 0:
        pares +=1
    else:
        impares += 1

print(f"Números ingresados:{numeros}")
print(f"Cantidad de números pares:{pares}")
print(f"Cantidad de números impares:{impares}")

### Ejercicio 4

alumnos= []
n= int(input("¿Cuántos alumnos desea ingresar?"))

for i in range(n):
    nombre= input("Ingrese el nombre del alumno: ")

    notas= []
    for j in range(3):
        nota=float(input(f"Ingrese la calificación {j+1} de {nombre}: "))
        notas.append(nota)
    
    alumno= {
        "Alumno": nombre,
        "Notas": notas
    }

    alumnos.append(alumno)

print("Listado completo de alumnos: ")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

### Ejercicio 5

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

suma_primos=0

for num in range(100):
    if primo(num):
        suma_primos += num
print ("La suma de todos los números primos menores que 100 es: ", suma_primos)
    







                   
                   





