import os

def crear_carpeta():
    if not os.path.exists("archivos"):
        os.makedirs("archivos")

def crear_html():
    contenido_html = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejemplo de etiquetas &lt;p&gt;</title>
</head>
<body>
    <h1>Ejemplo de etiquetas &lt;p&gt;</h1>

    <p>Este es un párrafo de texto.</p>

    <p>Este es otro párrafo de texto.</p>

    <p>Y aquí va un tercer párrafo de texto.</p>

    <p>¡Puedes añadir tantos párrafos como desees!</p>
</body>
</html>
    '''

    crear_carpeta()  # Crear carpeta si no existe
    ruta_archivo = os.path.join("archivos", "ejercicio12.html")

    # Escribir el contenido en un archivo HTML
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo_html:
        archivo_html.write(contenido_html)

# Llamamos a la función para generar el HTML
crear_html()

#1. Crea un archivo llamado "archivo.txt" y escribe en él "Hola, mundo!".

def Ejercicio1():
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo, "w") as Archivo1:
        Archivo1.write("Hola, mundo !")
print("#1. Crea un archivo llamado 'archivo.txt' y escribe en él 'Hola, mundo!'.")
Ejercicio1()

#2. Lee el contenido del archivo "archivo.txt" y muéstralo por pantalla.
def Ejercicio2():
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo,"r") as Archivo2:
        leer=Archivo2.read()
        print(leer)
print("#2. Lee el contenido del archivo 'archivo.txt' y muéstralo por pantalla.")
Ejercicio2()

#3. Añade "¡Python es increíble!" al final del archivo "archivo.txt".
def Ejercicio3():
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo,"a") as Archivo3:
        Archivo3.write("\n¡Python es increíble!")
print("#3. Añade '¡Python es increíble!' al final del archivo 'archivo.txt'.")
Ejercicio3()
#4. Cuenta cuántas líneas tiene el archivo "archivo.txt"
def Ejercicio4():
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo,"r") as Archivo4:
        longitud=Archivo4.readlines()
        print(len(longitud))
print("#4. Cuenta cuántas líneas tiene el archivo 'archivo.txt'")
Ejercicio4()

#5. Lee la segunda línea del archivo "archivo.txt".
def Ejercicio5():
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo,"r") as Archivo5:
        longitud=Archivo5.readlines()
        print(longitud[1])
print("#5. Lee la segunda línea del archivo 'archivo.txt'.")
Ejercicio5()
# # 6. Crea una copia del archivo "archivo.txt" llamada "copia_archivo.txt"
def Ejercicio6():
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo,"r") as Archivo6:
        contenido=Archivo6.read()
    ruta_archivo2 = os.path.join("archivos", "copia_archivo.txt")
    with open(ruta_archivo2,'w') as archivo:
        archivo.write(contenido)
print("#6. Crea una copia del archivo 'archivo.txt' llamada 'copia_archivo.txt'")
Ejercicio6()
# #7. Crea una función que reciba un nombre de archivo como parámetro y muestre su contenido por pantalla.
def Ejercicio7(Nombre_Archivo):
    with open(Nombre_Archivo,'r') as Archivo7:
        contenido=Archivo7.read()
        print(contenido)

print("#7. Crea una función que reciba un nombre de archivo como parámetro y muestre su contenido por pantalla.")
ruta_archivo = os.path.join("archivos", "archivo.txt")
Ejercicio7(ruta_archivo)

# #8. Crea una función que reciba un nombre de archivo como parámetro y devuelva la cantidad de caracteres que contiene
def Ejercicio8(Nombre_Archivo):

    with open(Nombre_Archivo,"r") as Archivo8:
        contenido=Archivo8.read()
        print(len(contenido))
print("#8. Crea una función que reciba un nombre de archivo como parámetro y devuelva la cantidad de caracteres que contiene")
ruta_archivo = os.path.join("archivos", "archivo.txt")
Ejercicio8(ruta_archivo)
#
# #9. Escribe una lista de números en un archivo llamado "numeros.txt", uno por línea.
def Ejercicio9():
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "numeros.txt")
    with open(ruta_archivo,'w') as Archivo9:
        for i in range(1,11):
            Archivo9.write(str(f'{i}\n'))
print("#9. Escribe una lista de números en un archivo llamado 'numeros.txt', uno por línea.")
Ejercicio9()
#
# #10. Lee el archivo "numeros.txt" y suma todos los números presentes en él.
def Ejercicio10():
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "numeros.txt")
    suma = 0
    with open(ruta_archivo, 'r') as Archivo10:
        for linea in Archivo10:
            numero = int(linea.strip())
            suma += numero
    return f"La suma de los números en el archivo es: {suma}"
    print("#10. Lee el archivo 'numeros.txt' y suma todos los números presentes en él.")
ejer10=Ejercicio10()
print(ejer10)
#
# #11. Escribe un programa que pida al usuario ingresar una línea de texto y la guarde en un archivo llamado "entrada_usuario.txt".
def Ejercicio11(Linea_Texto):
    crear_carpeta()
    ruta_archivo = os.path.join("archivos", "entrada_usuario.txt")
    with open(ruta_archivo,'w') as Archivo11:
        Archivo11.write(Linea_Texto)
print("#11. Escribe un programa que pida al usuario ingresar una línea de texto y la guarde en un archivo llamado 'entrada_usuario.txt'.")
texto=input("Esciba la linea de texto a ser ingresada: ")
Ejercicio11(texto)
#
# #12. Crea una función que tome un archivo HTML como entrada y cuente cuántas etiquetas <p> contiene.
def Ejercicio12():
    ruta_archivo = os.path.join("archivos", "ejercicio12.html")
    cont=0
    with open(ruta_archivo,'r') as Archivo12:
        for linea in Archivo12:
            if '<p>' in linea:
                cont+=1
    return f'La cantidad de etiquetas <p> en el archivo son {cont}'
print("#12. Crea una función que tome un archivo HTML como entrada y cuente cuántas etiquetas <p> contiene.")
ejer12=Ejercicio12()
print(ejer12)
#
# #13. Escribe un programa que reemplace todas las ocurrencias de una palabra específica en un archivo de texto.
def Ejercicio13(palabra1, palabra2):
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo, "r") as Arch_txt:
        contenido = Arch_txt.read()
        contenido = contenido.replace(palabra1, palabra2)
    with open(ruta_archivo, "w") as Arch_txt:
        Arch_txt.write(contenido)

print("#13. Escribe un programa que reemplace todas las ocurrencias de una palabra específica en un archivo de texto.")
Ejercicio13("increible","asombroso")

# # 14. Crea un programa que lea un archivo JSON y muestre solo los elementos que cumplen cierta condición.
import json

def Ejercicio14():
    ruta_archivo = os.path.join("archivos", "Ejercicio14.json")
    with open(ruta_archivo, 'w') as Archivo14:
        json.dump([
            {"nombre": "Juan", "edad": 25},
            {"nombre": "Ana", "edad": 35},
            {"nombre": "Pedro", "edad": 50}
        ], Archivo14)

    with open(ruta_archivo, 'r') as ArchivoLectura:
        contenido = json.load(ArchivoLectura)
        for i in contenido:
            if i['edad'] >= 30:
                print(i)
print("#14. Crea un programa que lea un archivo JSON y muestre solo los elementos que cumplen cierta condición.")
Ejercicio14()
#
# # 15. Crea un programa que concatene dos archivos de texto en uno nuevo.

def Ejercicio15():
    ruta_archivo = os.path.join("archivos", "archivo1.txt")
    with open(ruta_archivo, 'w') as Archivo1:
        Archivo1.write("Hola, mundo!")
    ruta_archivo1 = os.path.join("archivos", "archivo2.txt")
    with open(ruta_archivo1, 'w') as Archivo2:
        Archivo2.write("¡Python es increíble!")

    with open(ruta_archivo, 'r') as Archivo1, open(ruta_archivo1, 'r') as Archivo2:
        contenido1 = Archivo1.read()
        contenido2 = Archivo2.read()
    ruta_archivo2 = os.path.join("archivos", "archivo3.txt")
    with open(ruta_archivo2, 'w') as Archivo3:
        Archivo3.write(contenido1 + contenido2)

print("#15. Crea un programa que concatene dos archivos de texto en uno nuevo.")
Ejercicio15()
#
# # 16. Escribe una función que tome una lista de nombres y los escriba en un archivo de texto, uno por línea.
def Ejercicio16(Nombres):
    ruta_archivo = os.path.join("archivos", "nombres.txt")
    with open(ruta_archivo, 'w') as Archivo16:
        for i in Nombres:
            Archivo16.write(i + "\n")
print("#16. Escribe una función que tome una lista de nombres y los escriba en un archivo de texto, uno por línea.")
cantidad_Nombres = int(input("Ingrese la cantidad de nombres a ingresar: "))
Nombres = [input(f"Ingrese el {i} nombre: ") for i in range(1, cantidad_Nombres + 1)]
Ejercicio16(Nombres)

#
# # 17. Crea un programa que ordene alfabéticamente las líneas de un archivo de texto.
def Ejercicio17():
    ruta_archivo = os.path.join("archivos", "nombres.txt")
    with open(ruta_archivo, 'r') as Archivo17:
        contenido = Archivo17.readlines()
        contenido.sort()
    ruta_archivo1 = os.path.join("archivos", "nombres1.txt")
    with open(ruta_archivo, 'w') as Archivo17:
        for i in contenido:
            Archivo17.write(i)
print("#17. Crea un programa que ordene alfabéticamente las líneas de un archivo de texto.")
Ejercicio17()

# # 18. Escribe una función que lea un archivo de texto y elimine las líneas duplicadas.
def Ejercicio18():
    ruta_archivo = os.path.join("archivos", "nombres.txt")
    with open(ruta_archivo, 'r') as Archivo18:
        contenido = Archivo18.readlines()
        contenido = set(contenido)
    ruta_archivo1 = os.path.join("archivos", "nombres2.txt")
    with open(ruta_archivo1, 'w') as Archivo18:
        for i in contenido:
            Archivo18.write(i)
print("#18. Escribe una función que lea un archivo de texto y elimine las líneas duplicadas.")
Ejercicio18()
#
# # 19. Crea un programa que recorra todos los archivos de un directorio y muestre sus nombres.

def Ejercicio19(ruta_directorio):

    print(f"Archivos en la carpeta {ruta_directorio}:")
    for elemento in os.listdir(ruta_directorio):
        ruta_completa = os.path.join(ruta_directorio, elemento)
        if os.path.isfile(ruta_completa):  # Verificar si es un archivo
            print(f"Archivo: {elemento}")
        else:
            print(f"Directorio: {elemento}")

print("#19. Crea un programa que recorra todos los archivos de un directorio y muestre sus nombres.")
ruta_directorio = os.path.join("archivos")
Ejercicio19(ruta_directorio)
# # 20. Crea un programa que lea un archivo de texto y reemplace las vocales con acento por vocales sin acento.
def Ejercicio20():
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo, 'r') as Archivo20:
        contenido = Archivo20.read()
        contenido = contenido.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    ruta_archivo1 = os.path.join("archivos", "archivo4.txt")
    with open(ruta_archivo1, 'w') as Archivo20:
        Archivo20.write(contenido)
print("#20. Crea un programa que lea un archivo de texto y reemplace las vocales con acento por vocales sin acento.")
Ejercicio20()
# # 21. Escribe una función que lea un archivo de texto y cuente la cantidad de veces que aparece una palabra específica.
def Ejercicio21(palabra):
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    cont=0
    with open(ruta_archivo, 'r') as Archivo21:
        contenido = Archivo21.read()
        contenido = contenido.split()
        for i in contenido:
            print(i)
            if i == palabra:
                cont+=1
    return f"La palabra {palabra} aparece {cont} veces"
print("#21. Escribe una función que lea un archivo de texto y cuente la cantidad de veces que aparece una palabra específica.")
ejercicio21=Ejercicio21("mundo")
print(ejercicio21)

# # 22. Escribe una función que reciba el nombre de un archivo y devuelva la longitud del contenido más largo de una línea.
def Ejercicio22():
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo, 'r') as Archivo22:
        contenido = Archivo22.readlines()
        longitud = 0
        for i in contenido:
            if len(i) > longitud:
                longitud = len(i)
    return f"La longitud de la línea más larga es: {longitud}"
print("#22. Escribe una función que reciba el nombre de un archivo y devuelva la longitud del contenido más largo de una línea.")
ejercicio22=Ejercicio22()
print(ejercicio22)
#
# # 23. Implementa un programa que encuentre la palabra más larga en un archivo de texto
#
def Ejercicio23():

    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo, 'r') as Archivo23:
        contenido = Archivo23.read()
        contenido = contenido.split()
        longitud = 0
        for i in contenido:
            if len(i) > longitud:
                longitud = len(i)
                palabra = i
    return f"La palabra más larga es: {palabra}"
print("#23. Implementa un programa que encuentre la palabra más larga en un archivo de texto")
ejercicio23=Ejercicio23()
print(ejercicio23)
#
# # 24. Crea un programa que lea un archivo de texto y elimine todas las líneas en blanco.
def Ejercicio24():
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    with open(ruta_archivo, 'r') as Archivo24:
        contenido = Archivo24.readlines()
        contenido = [i for i in contenido if i != "\n"]
    ruta_archivo1 = os.path.join("archivos", "archivo5.txt")
    with open(ruta_archivo1, 'w') as Archivo24:
        for i in contenido:
            Archivo24.write(i)
print("#24. Crea un programa que lea un archivo de texto y elimine todas las líneas en blanco.")
Ejercicio24()
#
# # 25. Escribe una función que lea un archivo de texto y cuente cuántas vocales hay en él.
def Ejercicio25():
    ruta_archivo = os.path.join("archivos", "archivo5.txt")
    cont = 0
    with open(ruta_archivo, 'r') as Archivo25:
        contenido = Archivo25.read()
        for i in contenido:
            if i in "aeiou":
                cont += 1
    return f"La cantidad de vocales en el archivo es: {cont}"
print("#25. Escribe una función que lea un archivo de texto y cuente cuántas vocales hay en él.")
ejercicio25=Ejercicio25()
print(ejercicio25)
#
# # 26. Crea una función que lea dos archivos de texto, los compare y muestre las líneas que son iguales en ambos.
def Ejercicio26():
    ruta_archivo = os.path.join("archivos", "archivo.txt")
    ruta_archivo1 = os.path.join("archivos", "archivo5.txt")
    with open(ruta_archivo, 'r') as Archivo26, open(ruta_archivo1, 'r') as Archivo26_1:
        contenido1 = Archivo26.readlines()
        contenido2 = Archivo26_1.readlines()
        for i in contenido1:
            if i in contenido2:
                print(i)
print("#26. Crea una función que lea dos archivos de texto, los compare y muestre las líneas que son iguales en ambos.")
Ejercicio26()
# # 27. Escribe un programa que recorra todos los archivos de un directorio y muestre sus nombres junto con la cantidad de líneas que contienen
def Ejercicio27(ruta_directorio):
    print(f"#27. Escribe un programa que recorra todos los archivos de un directorio y muestre sus nombres junto con la cantidad de líneas que contienen en la carpeta {ruta_directorio}")
    for archivo in os.listdir(ruta_directorio):
        ruta_archivo = os.path.join(ruta_directorio, archivo)
        if os.path.isfile(ruta_archivo):  # Verificar si es un archivo
            with open(ruta_archivo, 'r') as archivo_actual:
                contenido = archivo_actual.readlines()
                print(f"El archivo {archivo} tiene {len(contenido)} líneas")

print("#27. Escribe un programa que recorra todos los archivos de un directorio y muestre sus nombres junto con la cantidad de líneas que contienen")
# Directorio 'archivos'
ruta_archivos = 'archivos'

# Llamada a la función para mostrar los archivos en la carpeta 'archivos' junto con la cantidad de líneas
Ejercicio27(ruta_archivos)