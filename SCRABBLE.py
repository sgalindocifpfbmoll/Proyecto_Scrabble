"""
PROYECTO SCRABBLE
Editores:   Salvador Galindo
            Facundo
            Juan
DOCUMENTO: https://docs.google.com/document/d/19qLfRDQjicCGriPfUQGNLpU69WttZMfHk9bWYa6U6Qg/edit

ANOTACIONES:
casillas=[i][j]=[num][letra] --> casillas=[[fila1][fila2]...[fila15]]
Tenemos en cuenta que num1=0 (posicion 0) y A=0 (posicion 0)
Para editar la puntuación de un jugador:
jugadores={0:datos1, 1:datos2, 2:datos3, 3:datos4} por lo tanto accedemos al valor de la clave
datosx=[puntos,letras]
letra=[puntuacion, numerodeletras]
"""

#--------------LISTAS, VARIABLES, CONSTANTES:----------------------
#Diccionario que contiene las letras y sus respectivas puntuaciones
letras = {"A": [1,9] , "B": [3,2] , "C": [3,2] , "D": [2,4] ,
             "E": [1,12] , "F": [4,2] , "G": [2,3] , "H": [4,2] ,
             "I": [1,9] , "J": [8,1] , "K": [5,1] , "L": [1,4] ,
             "M": [3,2] , "N": [1,6] , "O": [1,8] , "P": [3,2] ,
             "Q": [10,1], "R": [1,6] , "S": [1,4] , "T": [1,6] ,
             "U": [1,4] , "V": [4,2] , "W": [4,2] , "X": [8,1] ,
             "Y": [4,2] , "Z": [10,1]}
#Casillas: individual y listas (tablero)
casillas=[]
#Anchura y altura del tablero
HORIZONTAL=15
VERTICAL=15
#Declaración de valores globales
jugadores = dict()
turnoactual=0
puntuacionGanar=50
detectadasAntes=[] #palabras detectadas en cada turno



#------------------------REGLAS:----------------------------------
"""Mostrar reglas"""
def mostrarInstrucciones():
    print("===========================================================================================================================================")
    print("=                                                            REGLAS                                                                       =")
    print("===========================================================================================================================================")
    print("Cada jugador toma siete fichas de la bolsa. Cada ficha tiene una puntuación diferente.")
    print("El primer jugador debe formar una palabra usando dos o más letras, colocándola horizontalmente o verticalmente sobre el tablero.")
    print("El turno pasa entonces al segundo jugador que puede: añadir una o más letras a la palabra existente ampliándola y llevándose la puntuación")
    print("de esa palabra más la puntuación de las letras añadidas o formar una nueva palabra usando una letra de la existente, o ambas.")
    print("Un jugador  puede pasar sin cambiar ninguna ficha. Ello ocurre cuando tiene una palabra de alta puntuación en su raíl,")
    print("pero no existe letra en el tablero a la que conectarla. El jugador que acaba de tirar anota su puntuación,")
    print("basada en el valor total de las fichas que ha emplazado, toma las fichas que le hacen falta para sumar siete de la bolsa.")
    print("El segundo jugador debe, a continuación, colocar una o más letras, en línea recta, para formar al menos una nueva palabra.")
    print("El juego seguirá hasta que el total de fichas a repartir llegue a 0")
    print("============================================================================================================================================")
    print("=                                                            PUNTUACIÓN                                                                    =")
    print("============================================================================================================================================")
    print("Las letra A,E,I,O,U tienen un valor de 1 punto.")
    print("Las letras D y G tienen un valor de 2 puntos.")
    print("Las letras B,C,M y P tienen un valor de 3 puntos.")
    print("Las letras F,H,V,W e Y tienen un valor de 4 puntos.")
    print("La letra K tiene un valor de 5 puntos.")
    print("Las letras J y X tienen un valor de 8 puntos.")
    print("Las letras Q y Z tienen un valor de 10 puntos")
    print("============================================================================================================================================")      

#--------------------GETTERS & SETTERS:----------------------------
def devolverCasilla(i,j):
    return casillas[i][j]

def getPuntuacionJugador(turno):
    return jugadores.get(turno)[0]

def getLetrasJugador(turno):
    return jugadores.get(turno)[1]

def setPuntuacionJugador(turno, puntuacion):
    jugadores.get(turno)[0]+=puntuacion

def setLetraJugador(turno, letra):
    jugadores.get(turno)[1]+=letra

def getPuntuacionLetra(letra):
    return letras.get(letra)[0]

#--------------------PINTAR TABLERO:-------------------------------
""" Pintar tablero"""
def pintarTablero():
    print()
    c=0
    continuar=True
    while(continuar):
        #IMPRIME LAS LETRAS SUPERIORES E INFERIORES
        if(c==0 or c==4):
            for i in letras:
                if(i=="O"):
                    print(i)
                    break
                elif(i=="A"):
                    print("  ",i,end="  ")
                else:
                    print(i,end="  ")
            if(c==4):
                continuar=False
        #IMPRIME LAS LINEAS ENTRE LAS LETRAS Y LAS CASILLAS
        elif(c==1 or c==3):
            print("  ║",end="")
            for j in range(15):
                if(j==14):
                    print("═",end="")
                    print("║")
                else:
                    print("═══",end="")
        #IMPRIME EL CONTENIDO DEL TABLERO (LAS CASILLAS)
        else:
            filaNumero=True
            filaVacia=False
            i=0
            while(i<15):
                if(filaNumero):
                    filaNumero=False
                    filaVacia=True
                    if(-1<i<9):
                        print("",i+1,end="")
                    else:
                        print(i+1,end="")
                elif(filaVacia):
                    filaVacia=False
                    filaNumero=True
                    print("  ",end="")
                print("║",end="")
                for j in range(15):
                    if(not filaNumero):
                        if(j==14):
                            print(devolverCasilla(i,j)+"║",(str)(i+1))
                            i+=1
                        else:
                            print(devolverCasilla(i,j),end="  ")
                    elif(not filaVacia):
                        if(j==14):
                            print("","║")
                        else:
                            print(" ",end="  ")
        c+=1
        
#----------------------------MOSTRAR-----------------------------------    
""" Mostrar Turnos:"""
def mostrarTurnos():
    #Variables globales
    global turnoactual
    global jugadores
    #Variable local
    orden=["primer","segundo","tercer","cuarto"]
    c=0
    print()
    #Se imprimen los valores de turnos junto al jugador correspondiente.
    for i in jugadores:
        print("El",orden[c],"turno es: J"+(str)(i))
        c+=1
    #Se imprime el turno actual
    print("El turno actual es del jugador J"+(str)(turnoactual))
    
""" Mostrar puntuación total:"""
def mostrarPuntuacion():
    #Variables globales
    global turnoactual
    global jugadores
    #Variable local
    orden=["primer","segundo","tercer","cuarto"]
    print()
    #Se imprimen los valores de puntuación junto al jugador correspondiente.
    for i in jugadores:
        print("La puntuación de J"+(str)(i),"es de",getPuntuacionJugador(i),"puntos.")
        
""" Mostrar palabras en el tablero:"""
def mostrarPalabras():
    #Obtenemos la lista de palabras detectadas.
    palabrasTotal=detectarPalabras()
    #Si esta vacía se imprime:
    if(len(palabrasTotal)==0):
        print("\nNo hay palabras en el tablero.")
    else:
        print("\nPalabras en el tablero:\n")
        #Se imprimen las palabras del tablero.
        for palabra in palabrasTotal:
            print(palabra)

""" Mostrar letras que posee un jugador:"""
def mostrarLetras(turno):
    #Se imprime las letras que posee el jugador.
    print("        Letras disponibles:",getLetrasJugador(turno))

    
#-------------------------------ESCRIBIR----------------------------------------------
""" Escribir: permite al jugador escribir una palabra en el tablero y ganar puntos"""
def escribirPalabra():
    #Variables globales
    global turnoactual
    global jugadores
    global puntuacionGanar
    #Variables locales
    i=0
    continuar=True
    #Pide los datos: palabra, número y letra. Si se introduce un caracter incorrecto
    #devuelve error y pide el valor de nuevo.
    while (continuar):
        try:
            if(i==0):
                palabra=(input("¿Qué deseas escribir?: ")).upper()
                for j in palabra:
                    if(j not in letras):
                        raise errorPalabra
                i+=1
            elif(i==1):
                posNum=int(input("Introduce un número: "))-1
                if(-1<posNum<15):
                    i+=1
                else:
                    raise ValueError
            elif(i==2):
                letra=(input("Introduce una letra: ")).upper()
                if(letra not in letras or letra>"O"):
                    raise errorLetra
                else:
                    #Obtenemos la posición de la letra introducida:
                    posLetra=posicionLetra(letra)
                    i+=1
            elif(i==3):
                sentido=int(input("Escribe un sentido (1. Derecha/2. Abajo): "))
                if(sentido!=1 and sentido!=2):
                    raise ValueError
                else:
                    continuar=False
        except ValueError:
            print("    Error. Introduce un número válido.")
        except errorLetra:
            print("    Error. Introduce una letra válida.")
        except errorPalabra:
            print("    Error. Introduce una palabra con caracteres alfabéticos.")
    #Insertamos los datos y comprobamos si la palabra se puede introducir en el tablero:
    colocarTablero=comprobarTablero(palabra,posNum,posLetra,sentido)
    #No se puede introducir. Lanzamos error y al menú jugador.
    if(colocarTablero==False):
        print("\n    Error. La palabra no se puede colocar en el tablero.\n")
    #La palabra se puede escribir en el tablero. Continuamos.
    else:
        #Comprobamos si el jugador tiene las letras:
        colocarLetras=comprobarLetras(getLetrasJugador(turnoactual),colocarTablero)
        #No las tiene, lanzamos error y volvemos al menú jugador.
        if(colocarLetras==False):
            print("\n    Error. No tienes las suficientes letras para colocar la palabra",palabra,".")
        #El jugador tiene las letras.Colocamos las casillas.
        else:
            for letra in palabra:
                #Se coloca la letra en la casilla indicada
                casillas[posNum][posLetra]=letra
                #Y depende del sentido sumamos una casilla al numero o letra
                if(sentido==2):
                    posNum+=1
                if(sentido==1):
                    posLetra+=1
            #Pintamos el tablero:
            pintarTablero()
            #La palabra se ha escrito. Se suman los puntos y se imprimen:
            print("\nEl Jugador",turnoactual,"ha sumado",sumarPuntuacion(),"puntos.")
            print("Su puntuación total es de",getPuntuacionJugador(turnoactual),"puntos.")
            #Comprobamos si el jugador ha llegado a ganar la partida: 50 puntos.
            if(getPuntuacionJugador(turnoactual)>=puntuacionGanar):
                ganarPartida(turnoactual)
            #Si no, gasta las letras y damos las nuevas que falten al jugador,
            #y pasa turno al siguiente jugador
            else:
                gastarLetrasJugador(turnoactual,palabra)
                print("Ha obtenido las siguientes letras:",obtenerLetras(turnoactual))
                siguienteJugador()

#----------------------- AFECTA A JUGADORES ---------------------------------------
""" Crear jugadores: crea un diccionario que contiene a los jugadores requeridos
    con su respectiva información: sus puntuaciones y letras.Se guarda en jugadores."""
def crearJugadores(numJugadores):
    import random
    #Variables globales
    global turnoactual
    global jugadores
    #Variable local
    i=1
    while(i<numJugadores+1):
        secreto=random.randint(1,numJugadores)
        if(secreto not in jugadores):
            if(i==1):
                turnoactual=secreto
            jugadores[secreto]=[0,""]
            obtenerLetras(secreto)
            i+=1

""" Sumar puntuación: suma los puntos correspondientes a la puntuacion del
    jugador correspondiente. Obtiene las nuevas palabras escritas y las recorre para
    detectar qué letras tienen. Según cada letra suma una puntuación diferente.
    Devuelve la puntuación que se acaba de obtener y manipula la punt del jugador."""
def sumarPuntuacion():
    #Variables globales
    global turnoactual
    global letras
    global jugadores
    #Variables locales
    puntuacion=0
    nuevasPalabras=detectarPalabrasNuevas()
    #Recorremos las letras de nuevas palabras y vamos
    #sumando la puntuación correspondiente a la letra:
    #Recorremos las palabras
    for i in nuevasPalabras:
        #Recorremos las letras
        for j in i:
            if(j in letras):
                puntuacion+=letras.get(j)[0]
    #Se suman los puntos al jugador correspondiente
    setPuntuacionJugador(turnoactual,puntuacion)
    #Y se devuelve la puntuación obtenida en este turno
    return puntuacion

""" Siguiente jugador: """
def siguienteJugador():
    #Variables globales
    global turnoactual
    global jugadores
    #El turno actual obtiene el valor de la siguiente posición del orden
    #Pasamos jugadores a una lista para recorrerla con orden
    ordenJugadores=[(i) for i in jugadores.keys()]
    if(ordenJugadores.index(turnoactual)==len(ordenJugadores)-1):
        turnoactual=ordenJugadores[0]
    else:
        turnoactual=ordenJugadores[ordenJugadores.index(turnoactual)+1]

""" Gastar letras Jugador"""
def gastarLetrasJugador(turno,palabra):
    for letra in palabra:
        jugadores.get(turno)[1]=getLetrasJugador(turno).replace(letra,"",1)

def ganarPartida(turno):
    print("Se acabó la partida. El jugador J"+(str)(turno),"ha ganado la partida con"
          ,getPuntuacionJugador(turno),"puntos.")
    menuPrincipal()
        
#---------------------------------AFECTA A LETRAS-----------------------------------
""" Gastar Letra Letras: resta 1 al número total de la cantidad de la letra
    introducida."""
def gastarLetraLetras(letra):
    if(letras.get(letra)[1]>0):
        letras.get(letra)[1]-=1
        return True
    else:
        return False

#--------------------------- TABLERO: ------------------------------------------
"""Crear Tablero: crea una lista con listas que sirven como casillas."""
def crearTablero():
    for i in range(VERTICAL):
        casillashorizontal=[]
        for j in range(HORIZONTAL):
            casillashorizontal.append("■")
        casillas.append(casillashorizontal)
        
""" Comprobar tablero: comprueba si la palabra escrita se puede insertar en la posición
    especificada. Parámetros: posNum, posLetra, palabra y sentido.
    Devuelve True si la palabra se puede escribir, False si no se puede escribir. """
def comprobarTablero(palabra,posNum,posLetra,sentido):
    #Variable local
    longitud=0
    #Determinamos la longitud total según el sentido
    if(sentido==1):
        longitud=posLetra+len(palabra)
    elif(sentido==2):
        longitud=posNum+len(palabra)
    #Si su posición excede el tablero se devuelve False
    if(longitud > 15):
        return False
    else:
        for letra in palabra:
            if(casillas[posNum][posLetra]=="■"):
                pass
            elif(casillas[posNum][posLetra]==letra):
                palabra=palabra.replace(letra,"",1)
            else:
                return False
            if(sentido==1):
                posLetra+=1
            elif(sentido==2):
                posNum+=1
        return palabra

""" Comprobar Letras:
    Parámetros: letras: lista las letras que tiene el usuario.
                palabra: lista con las letras que necesita el usuario. """
def comprobarLetras(letras,palabra):
    #Recorremos las letras de la palabra
    for letra in palabra:
        #Si la letra no está en letras del jugador devolvemos false
        if(letra not in letras):
            return False
        #Si está, quitamos la letra (1) de letras del jugador
        #para no recorrerla de nuevo
        else:
            letras=letras.replace(letra,"",1)
    #Se ha recorrido hasta el final. Jugador tiene trodas las letras.
    return True

""" Posicion de la letra: obtenemos la posicion de una letra que insertamos como
    parámetro y nos devuelve la posición en el abecedario."""
def posicionLetra(letraIntroducida):
    posLetra=0
    for letra in letras:
        if(letra==letraIntroducida):
            return posLetra
        posLetra+=1
    return False

""" Obtener Letras: devuelve un número determinado de letras al jugador.
    LetrasJugador es una string que contiene las letras del jugador.""" 
def obtenerLetras(turno):
    import random
    import string
    #Variable local
    letrasNuevas=""
    #Mientras el jugador no tenga 7 letras
    while(len(getLetrasJugador(turno))!=7):
        #Obtenemos una random del abecedario
        letra=(random.choice(string.ascii_letters)).upper()
        #Si la letra random se puede obtener (hay cantidad>0 de esa letra)
        if(gastarLetraLetras(letra)==True):
            #La letra random se inserta en letrasNuevas y se añade al jugador
            letrasNuevas+=letra
            setLetraJugador(turno,letra)
    return letrasNuevas

""" Detectar palabras: detecta palabras en el tablero y las suma a una lista
    palabrasTotales."""
def detectarPalabras():
    #Variables globales
    global detectadasTotal
    #Variables locales
    palabras=[]
    detectadas=[]
    detHorizontal=[]
    detVertical=[]
    #Detecta palabras horizontales
    for i in range(VERTICAL):
        for j in range(HORIZONTAL):
            #Si la casilla no es un espacio vacío
            if(casillas[i][j]!="■"):
                #Añadimos la letra a la lista de la palabra
                detHorizontal.append(casillas[i][j])
                if(j==HORIZONTAL-1):
                    if(len(detHorizontal)>1):
                        detectadas.append(detHorizontal)
                    detHorizontal=[]
                elif(casillas[i][j+1]=="■"):
                    if(len(detHorizontal)>1):
                        detectadas.append(detHorizontal)
                    detHorizontal=[]
    #Detecta palabras verticales
    for j in range(HORIZONTAL):
        for i in range(VERTICAL):
            if(casillas[i][j]!="■"):
                detVertical.append(casillas[i][j])
                if(i==VERTICAL-1):
                    if(len(detVertical)>1):
                        detectadas.append(detVertical)
                    detVertical=[]
                elif(casillas[i+1][j]=="■"):
                    if(len(detVertical)>1):
                        detectadas.append(detVertical)
                    detVertical=[]
    #Inserta las palabras en forma de String en la lista palabras
    for i in range(len(detectadas)):
        palabras.append(listaToString(detectadas[i]))
    return palabras

""" Detectar palabras nuevas: """
def detectarPalabrasNuevas():
    #Variables globales
    global detectadasAntes
    #Variables locales
    nuevasPalabras=[]
    #Obtenemos el total de palabras en el tablero actual
    palabrasTotal=detectarPalabras()
    #Obtenemos la diferencia entre las palabras actuales y las del anterior turno
    #y las guardamos en nuevasPalabras
    nuevasPalabras=diferenciaListas(palabrasTotal,detectadasAntes)
    #Y las palabras del anterior turno obtienen el valor del turno actual
    detectadasAntes=palabrasTotal
    return nuevasPalabras
    
""" Convierte una lista de caracteres a String"""
def listaToString(lista):
    #Variables locales
    String=""
    for i in lista:
        String+=i
    return String

""" Diferencia Listas: devuelve los valores de diferencia entre 2 listas.
    Las listas deben ser simples, no listas de listas."""
def diferenciaListas(lista1, lista2): 
    return (list(set(lista1) - set(lista2))) 



#----------------------ERRORES---------------------------

# Errores definidos
class Error(Exception):
   """Error de base para otras excepciones"""
   pass

class errorLetra(Error):
    """Error letra"""
    pass

class errorPalabra(Error):
    """Error palabra"""
    pass

#-------------------------------------- MENUS -------------------------------    
""" Menú jugador:"""
def menuJugador():
    #Variables globales
    global turnoactual
    #Se pinta el tablero inicial
    print("\n Este es el tablero:")
    pintarTablero()
    #Y se muestra en pantalla
    mostrarTurnos()
    #Comienza el juego
    print("\nComienza el juego!!!")
    presionaEnter()
    print("\nMenú de juego:")
    salir=True
    i=0
    while(salir):
        print("\n------------------------------------------------")
        print("             Turno del Jugador",turnoactual)
        #Mostramos las letras que posee el jugador
        mostrarLetras(turnoactual)
        print("--------------------------------------------------")
        print("\n1. Escribir una palabra.")
        print("2. Pasar turno.")
        print("3. Ver Tablero.")
        print("4. Ver palabras en el tablero.")
        print("5. Ver el orden de juego y a cual es el turno actual.")
        print("6. Ver la puntuación actual total.")
        print("0. Salir.")
        try:
            opcion=int(input("Elige que hacer: "))
            if(opcion==1):
                escribirPalabra()
                presionaEnter()
            elif(opcion==2):
                opcion2=input("¿Estás seguro? Escribe "+"S"+" para"
                              " confirmar. Enter/otro caracter para continuar: ").upper()
                if(opcion2=="S"):
                    siguienteJugador()
            elif(opcion==3):
                pintarTablero()
            elif(opcion==4):
                mostrarPalabras()
                presionaEnter()
            elif(opcion==5):
                mostrarTurnos()
                presionaEnter()
            elif(opcion==6):
                mostrarPuntuacion()
                presionaEnter()
            elif(opcion==0):
                salir=False
            else:
                raise ValueError
        except ValueError:
            print("\n    Error.Introduce un número válido.")

def menuPrincipal():
    crearTablero()
    salir=True
    while(salir):
        print("------------------------------------------")
        print("                 SCRABBLE")
        print("------------------------------------------")
        print("\nMenú principal:")
        print("\n1. Jugar al SCRUBBLE.")
        print("2. Ver las instrucciones de juego.")
        print("0. Salir.")
        try:
            opcion=int(input("\nElige que hacer: "))
            if(opcion==1):
                numJugadores=int(input("\n¿Cuántos jugadores van a jugar? (2-4)? "))
                if(1<numJugadores<5):
                    #Se crean los jugadores necesarios y su orden
                    crearJugadores(numJugadores)
                    #Y nos lleva al menú jugador
                    menuJugador()
                else:
                    raise ValueError
            elif(opcion==2):
                mostrarInstrucciones()
            elif(opcion==0):
                salir=False
            else:
                raise ValueError
        except ValueError:
            print("\n    Error.Introduce un número válido.\n")

def presionaEnter():
    input("\nPresiona Enter para continuar.")            

#------------------------INICIO:-------------------------------------

#Inicio del programa            
menuPrincipal()
