# Reto3 MisionTic2022
def ruteo (distancias:dict, ruta_inicial:list)-> dict:    
    # Llamado funcion para validar el diccionario
    validarDistancias: bool = validar_distancias(distancias)     
    # Modelar Nodos
    if (validarDistancias == True) :            
        # Iniciar Variables                
        rutaActual = ruta_inicial.copy() # Copiar Lista
        mejoroDistancia:bool= False # Reinicia cada iteracion   
        rutaIteracion = rutaActual.copy() # Copiar Lista
        distancia = calcular_distancia(distancias, rutaIteracion)
        i = 0
        # Llamado Funcion determinar Arcos para iterar
        posiblesParejas:list = posibles_parejas(rutaIteracion)        
        # diccionario.keys() diccionario.values() diccionario.items()
        # Iteraciones de la solucion por intercambio de dos paradas
        while i < 1 :
            for pareja in posiblesParejas:
                # Llamado Funcion Transponer Arco
                rutaIntercambio = ejecutar_cambio(pareja, rutaActual)
                # Llamado Funcion Calcular Distancia
                distanciaIntercambio = calcular_distancia(distancias, rutaIntercambio)
                distanciaIteracion = calcular_distancia(distancias, rutaIteracion)
                # Modelar Nodos Visitados
                if distanciaIntercambio < distanciaIteracion :                
                    mejoroDistancia = True
                    rutaIteracion = rutaIntercambio
                    distancia = distanciaIntercambio
            # Preparar diccionario de salida
            if mejoroDistancia == True:
                mejoroDistancia = False # Reiniciar iteracion
                rutaActual= rutaIteracion.copy() # Copiar Lista
                rutaFinal = escribir_ruta(rutaActual)
                i = 0
            else:
                salida = {'ruta': rutaFinal, 'distancia': distancia}
                return salida
    else:
        errorMessage= ['Por favor revisar los datos de entrada.']
        return errorMessage[0]

# Funciones Auxiliares
def validar_distancias(distancias:dict) -> bool :
    # Variables
    distancias_1 = distancias.copy()
    validado = False    
    # Mensaje o validacion 
    for key1, key2 in distancias_1:
        key = (key1, key2) # tupla arco 
        value = distancias_1[key] # distancia almacenada
        # Validaciones distancia positiva
        if (value >= 0):
            validado = True
        else:
            validado = False
            break
        # Validaciones parametro de distancia entre el mismo nodo
        if (key[0] == key[1]):
            if (value == 0):
                validado = True
            else:
                validado = False
                break
    if validado == True:
        return validado
    else:
        return False

def calcular_distancia (distancias:dict, ruta_inicial:list)-> int:
    # Variables
    distancias_1 = distancias.copy() 
    rutaActual = ruta_inicial.copy()
    numeroNodos = len(rutaActual) - 1
    i = 0
    sumaDistancias = 0
    #
    for i in range( 0 , numeroNodos):
        j= i+1
        arco = ( rutaActual[i], rutaActual[j] )
        distanciaArco = distancias_1[arco]
        sumaDistancias += distanciaArco
    return sumaDistancias

def posibles_parejas (ruta_inicial:list)-> list:
    # Variables
    rutaActual = ruta_inicial.copy()
    numeroNodos = len(rutaActual) - 1
    i = 0
    j = 0
    arcosComparacion = []
    #
    for i in range( 1 , numeroNodos-1):
        for j in range( i+1 , numeroNodos):
            arco = ( rutaActual[i], rutaActual[j] )
            arcosComparacion += [arco]
    return arcosComparacion  

def ejecutar_cambio (arco: tuple, ruta_actual:list)-> list:
    # Variables
    nuevaRuta = ruta_actual.copy()
    # Identificar indice de posicion en la ruta
    for nodoX, nodoY in [arco]:
        indices = [nuevaRuta.index(nodoX), nuevaRuta.index(nodoY)]
        # Cambio de posiciones en la ruta
        for indiceX, indiceY in [indices]:
            nuevaRuta[indiceX]= nodoY
            nuevaRuta[indiceY]= nodoX
    return nuevaRuta

def escribir_ruta (ruta_actual:list) -> str:
    rutaActual = ruta_actual.copy()
    rutaFinal = ''
    for nodo in rutaActual:
        rutaFinal += str(nodo) + '-' 
    cadena = len(rutaFinal) - 1
    return rutaFinal[0:cadena]

distancias_1= {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41, ('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109, ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}
ruta_1= ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']
print(ruteo(distancias_1,ruta_1)) #{'ruta': 'H-A-F-B-D-C-E-H', 'distancia': 458}

distancias_2= {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27, ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117, ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199, ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19, ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31, ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}
ruta_2= ['H', 'B', 'E', 'A', 'C', 'D', 'H']
print(ruteo(distancias_2,ruta_2)) #{'ruta': 'H-D-A-B-C-E-H', 'distancia': 393}

distancias_3 = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41, ('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 555, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109, ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}
ruta_3= ['H', 'B', 'D', 'A', 'F', 'C', 'E', 'H']
print(ruteo(distancias_3,ruta_3))