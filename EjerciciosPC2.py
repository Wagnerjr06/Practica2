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

### Ejercicio 6

def fibonacci_secuencia():
    fib_secuencia= [0,1]
    while True:
        next_fib = fib_secuencia[-1] + fib_secuencia[-2]
        if next_fib > 50:
            break
        fib_secuencia.append(next_fib)
    return fib_secuencia

fib_numbers = fibonacci_secuencia()
print(fib_numbers)

### Ejercicio 7

def numero_perfecto(num):
    suma_divisores=0
    for i in range(1,num):
        if num % i == 0:
            suma_divisores += i
    return suma_divisores == num

def numeros_perfectos_menores_1000():
    perfectos = []
    for num in range(1,1000):
        if numero_perfecto(num):
            perfectos.append(num)
    return perfectos

numeros_perfectos = numeros_perfectos_menores_1000()
print("Numeros perfectos menores que 1000: ", numeros_perfectos)

### Ejercicio 8

def factorial(n):
    if n < 0:
        return "El factorial no está definidi para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2,n+1):
            resultado *= 1
        return resultado
    
numero=int(input("Introduce un número entero no negativo: "))
print(f"El factorial del {numero} es {factorial(numero)}")

### Ejercicio 9

def eliminar_vocales(texto):
    vocales = "AEIOUaeiou"
    resultado = ""
    for caracter in texto:
        if caracter not in vocales:
            resultado += caracter
    return resultado

entrada= input("Introduce un texto: ")

texto_sinvocales = eliminar_vocales(entrada)
print("Texto sin vocales: ", texto_sinvocales)

### Ejercicio 10

meses = [

    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
    "Agosto", "Septiembre", "Octubre", "Noviembre" , "Diciembre"
]

def convertir_fecha(fecha):
    if "/" in fecha:
        partes= fecha.split("/")
        mes = partes [0]
        dia = partes [1]
        año = partes [2]

        mes = mes.zfill(2)
        dia = dia.zfill(2)

        return f"{año}-{mes}-{dia}"
    else:
        partes= fecha.replace(",","").split()
        mes_nombre = partes[0]
        dia = partes [1]
        año = partes [2]

        if mes_nombre in meses:
            mes = str(meses.index(mes_nombre)+ 1).zfill(2)
        else:
            return "Mes no válido"
        
        dia = dia.zfill(2)

        return f"{año}-{mes}-{dia}"
    
entrada_usuario=input("Introduzca una fecha en formato MM/DD/AAAA o 'Mes Día, Año': ")

fecha_convertida = convertir_fecha(entrada_usuario)
print("Fecha convertida", fecha_convertida)











                   
                   





