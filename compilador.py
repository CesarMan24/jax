# definicion de palabras reservadas (solo minúsculas según la tabla)
KEYWORDS = ['leg', 'back', 'bic', 'tric', 'sho', 'day', 'ex', 'repeat', 'si', 'chest', 'sets', 'reps', 'weight', 'remaining', 'prn', 'num', 'end', 'gym']

# tipos de variables reconocidos
Variable_Types = ['leg', 'num', 'chest', 'sho', 'tric', 'back', 'bic', 'word']

# tablas de símbolos - Inicialización de tablas
Nombres = []
Tipo = []
Tamano = []
Dimension = []
DeclarationLine = []
UsageLine = []

# funcion principal para abrir el archivo y comenzar el análisis
def openjax():
    with open('pruebas.txt', 'r', encoding='utf-8') as file:
        contents = file.read()
        analizador(contents)
        
        # Mostrar tabla de símbolos al final
        print("\n")
        print("TABLA DE SÍMBOLOS:")
        print(" NOMBRE   TIPO   TAMANO   DIMENSION   DECLARATIONLINE   USAGELINE")
        for variable in range(len(Nombres)):
            print(f"{Nombres[variable]:<8} {Tipo[variable]:<6} {Tamano[variable]:<7} {Dimension[variable]:<10} {DeclarationLine[variable]:<16} {UsageLine[variable]}")

# funcion para analizar el código fuente
def analizador(contents):
    Await_type = " "  # Variable para controlar qué tipo de variable estamos esperando
    linea_codigo = 1
    contador = 0
    codigo = len(contents)
    parentesisabiertos = 0
    llavesabiertos = 0

    while contador < codigo:
        caracter = contents[contador]

        # ignorar espacios, saltos de línea, tabs
        if caracter in ['\n', '\t', ' ']:
            if caracter == '\n':
                linea_codigo += 1
            contador += 1
            continue

        # ignorar comentarios (%) *****(agregar lo que diko el ceasar de lo de cerrar)******
        elif caracter == '%':
            contador = procesar_comentario(contents, contador)

        # keywords e identificadores (empiezan con letra)
        elif caracter.isalpha():
            token, contador, nuevo_await_type = procesar_palabra(contents, contador, linea_codigo, Await_type)
            if nuevo_await_type != " ":
                Await_type = nuevo_await_type
            else:
                Await_type = " "  # resetea despuess de proc esar el identificador
        
        # numeross 
        elif caracter.isdigit():
            token, contador = procesar_numero(contents, contador)

        # operadores (=, +, <, >, -)
        elif caracter in ['=', '+', '<', '>', '-']:
            procesar_operador(caracter)
            contador += 1

        # punctuación ({, }, (, ), ,, ;)
        elif caracter in ['{', '}', '(', ')', ',', ';']:
            contador = procesar_puntuacion(caracter, contador, parentesisabiertos, llavesabiertos)
            if caracter == '(':
                parentesisabiertos += 1
            elif caracter == ')':
                parentesisabiertos -= 1
            elif caracter == '{':
                llavesabiertos += 1
            elif caracter == '}':
                llavesabiertos -= 1

        else:
            print(f"Error léxico en línea {linea_codigo}: caracter no reconocido '{caracter}'")
            contador += 1
    
    # Verificar balance de paréntesis y llaves
    if llavesabiertos != 0:
        print("Error Léxico: llaves desbalanceadas")
        return
    if parentesisabiertos != 0:
        print("Error Léxico: paréntesis desbalanceados") 
        return

# funcion para procesar comentarios (osea ignorar)
def procesar_comentario(contents, contador):
    # Ignorar hasta el final de la línea
    while contador < len(contents) and contents[contador] != '\n':
        contador += 1
    return contador

# funcion para procesar palabras (keywords o identificadores)
def procesar_palabra(contents, contador, linea_codigo, await_type):
    cadena = ""
    nuevo_await_type = " "
    
    # Lee la primera letra
    if contents[contador].isalpha():
        cadena += contents[contador]
        contador += 1
        
        # va seguir leyendo según el tipo de palabra
        # si es mayúscula, es identificador (puede tener números)
        if cadena[0].isupper():
            #identificadores: [A-Z][A-Z0-9]*
            while contador < len(contents) and (contents[contador].isupper() or contents[contador].isdigit()):
                cadena += contents[contador]
                contador += 1
            
            print(f"<IDENTIFICATOR, {cadena}>")
            
            # nanejo de tabla de símbolos para identificadores
            if await_type != " ":
                # es una declaración de variable
                Nombres.append(cadena)
                Tipo.append(await_type)
                Tamano.append(len(cadena))
                if await_type == "word":
                    Dimension.append(1)
                else:
                    Dimension.append(0)
                DeclarationLine.append(linea_codigo)
                UsageLine.append([linea_codigo])  # lista para múltiples usos
            else:
                #es un uso de variable
                if cadena in Nombres:
                    posicion_identificador = Nombres.index(cadena)
                    if isinstance(UsageLine[posicion_identificador], list):
                        UsageLine[posicion_identificador].append(linea_codigo)
                    else:
                        # convertir a lista si no lo es
                        UsageLine[posicion_identificador] = [UsageLine[posicion_identificador], linea_codigo]
                else:
                    print(f"Error: Identificador '{cadena}' no declarado en línea {linea_codigo}")
        
        else:
            # keywords: solo minúsculas [a-z]+
            while contador < len(contents) and contents[contador].islower():
                cadena += contents[contador]
                contador += 1
            
            if cadena in KEYWORDS:
                print(f"<KEYWORD, {cadena}>")
                
                # si la keyword es un tipo de variable, establecer await_type
                if cadena in Variable_Types:
                    nuevo_await_type = cadena
            else:
                # si no es keyword pero es solo minúsculas, podría ser un identificador no válido
                print(f"Error: '{cadena}' no es una palabra clave válida")

    return cadena, contador, nuevo_await_type

# funcion para procesar números (solo enteros)
def procesar_numero(contents, contador):
    cadena = ""
    
    # numeros enteros: [0-9]+
    while contador < len(contents) and contents[contador].isdigit():
        cadena += contents[contador]
        contador += 1

    print(f"<NUMERO, {cadena}>")
    return cadena, contador

# funcion para procesar operadores
def procesar_operador(caracter):
    print(f"<OPERATOR, {caracter}>")

# funcion para procesar puntuación
def procesar_puntuacion(caracter, contador, parentesisabiertos, llavesabiertos):
    print(f"<PUNCTUATION, {caracter}>")
    return contador + 1

# ejecutar el analizador
openjax()