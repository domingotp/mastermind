# Mastermind

from random import choice,randint                                                                       
from colorama import Fore,Style
from time import sleep
from os import system, name

def clear():                                    # Defino clear
    if name == 'nt':                            # Con este clear, podré limpiar el terminal para que el usuario solo vea
        _ = system('cls')                       # la información necesaria en ese momento.
    else:                                       # El primer if, detecta si el SO es Windows y el segundo si es Linux o MacOS
        _ = system('clear') 

def cargando(tipo,rep):                         # Defino cargando
    if tipo=='':                                # Básicamente esta función añade la animación de carga añadiendo 3 puntos (...) y borrando
        tipo='Cargando'                         # la pantalla para que se muestre la animación.
    i=1                                         # Le podemos definir el mensaje que sale antes de los 3 puntos.
    cont=1                                      # En caso de que no especifique nada se le asignará 'Cargando' por defecto.
    while True:                                 # En una última modificación le he añadido la opción 'rep' que me permite decirle
        if i>3:                                 # a la función cuantas veces quiero que se repita la animación de salir.
            i=1
        print(tipo+i*'.')
        sleep(1)
        clear()
        i+=1
        cont+=1
        if cont==rep*3:
            break

clear()                 # Limipiamos la pantalla antes de empezar

l1=[]

dificultad='facil'                       # Dificultad facil preestablecida.
longitud=4                               # Esta variable es para almacenar las longitudes de la contraseña dependiendo del nivel.


menu=True


print(Fore.RED+"███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗██████╗░")
print(Fore.RED+"████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗")
print(Fore.LIGHTYELLOW_EX+"██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║██║░░██║")
print(Fore.LIGHTYELLOW_EX+"██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██║░░██║")            # Letras inicio del programa
print(Fore.RED+"██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██████╔╝")
print(Fore.RED+"╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░\n")
#sleep(2)
print(Fore.BLUE+"█▄▄ █▄█   █▀▄ █▀█ █▀▄▀█ █ █▄░█ █▀▀ █▀█   ▀█▀ ▄▀█ █▀█ █▀█ ▄▀█ ▀█ █▀█ █▄░█ ▄▀█")
print(Fore.BLUE+"█▄█ ░█░   █▄▀ █▄█ █░▀░█ █ █░▀█ █▄█ █▄█   ░█░ █▀█ █▀▄ █▀▄ █▀█ █▄ █▄█ █░▀█ █▀█"+Style.RESET_ALL)


#################################
#      INICIO DEL PROGRAMA      #
################################# 


print("\nBienvenido a Mastermind")                                                              

nombre=input(Fore.CYAN+"Introduce tú nombre de usuario\U0001F4DD: "+Fore.MAGENTA)                         # NOMBRE DEL JUGADOR
print(Style.RESET_ALL)

while nombre=='':                                                                               # Si no introduce un nombre le pregunto si quiere añadir uno.
    otro=input("No has introducido ningún nombre, ¿quieres introducir otro? (s/n): ")           # Preguntamos si quiere poner otro nombre.
    while otro!="s" and otro!="S" and otro!="n" and otro!="N":                                  # Comprobación s/S/n/N 
        print(Fore.RED+"Opción no válida."+Style.RESET_ALL)
        otro=input("No has introducido ningún nombre, ¿quieres introducir otro? (s/n): ")   

    if otro=="s" or otro=="S":                                                                  # Comprobamos si quiere seguir o no.
        nombre=input(Fore.CYAN+"Introduce tú nombre de usuario: "+Fore.MAGENTA)                 # Vuelve a introducir el nombre de usuario.
        print(Style.RESET_ALL)
    else:
        nombre='Jugador'                                                                        # Al no querer introducirlo, le ponemos uno por defecto llamado Jugador.

print("\nNombre de jugador: "+Fore.YELLOW+nombre+Style.RESET_ALL)



##################
#      MENÚ      #
##################
while menu:
    clear()
    print(44*'#')
    print('#'+'\U0001F4E6 MENU \U0001F4E6'.center(40,' ')+'#')          # Cartel Menu
    print(44*'#')

    if dificultad=='facil':                     
        dd=Fore.GREEN+'Fácil'+Style.RESET_ALL                          
    elif dificultad=='medio':   
        dd=Fore.LIGHTYELLOW_EX+'Medio'+Style.RESET_ALL          # Aplicamos el estilo de la dificultad cambiando su color dependiendo de que dificultad sea y luego la podemos ver en el menú.
    else:
        dd=Fore.RED+'Difícil'+Style.RESET_ALL

    print(Fore.BLUE+'\n1.- Jugar \U0001F3AE '+Fore.WHITE+'Dificultad: '+dd)                     # Opción 1 jugar + dificultad seleccionada
    print(Fore.BLUE+'2.- Ajustes \U0001F9F0 '+Fore.CYAN+'(Selección de dificultad)')     # Opción 2 ajustes; Cambiar entre las 3 dificultades + características de cada dificultad
    print(Fore.BLUE+'3.- Instrucciones de juego \U0001F9E9')                                    # Instrucciones del juego
    print(Fore.LIGHTRED_EX+'4.- Salir')                                                         # Cerrar el programa
    print(Fore.YELLOW+'Usuario: '.rjust(50,' ')+Fore.LIGHTGREEN_EX+nombre+Style.RESET_ALL)      # Nombre del usuario en el menú
    m1=int(input('\nSelecciona una opción: '))
    while m1!=1 and m1!=2 and m1!=3 and m1!=4:
        print(Fore.RED+'¡La opción que has introducido no es válida!'+Style.RESET_ALL)      # Comprobación de menú; Comprobar que ha seleccionado una de las opciones.
        m1=int(input('\nSelecciona una opción: '))
        
    clear()         # Limpiar pantalla para el siguiente menú 


    if m1==2:               # Detectamos si ha elegido la segunda opción, ajustes.
        print(42*'#')
        print('#'+'SELECTOR DE DIFICULTAD'.center(40,' ')+'#')      # Cabecera
        print(42*'#')
        print(Fore.MAGENTA+'\n1.- '+Fore.GREEN+'Fácil'+Fore.WHITE+':')              # Introducción de las dificultades con sus características
        print(Fore.WHITE+'Longitud de la contraseña: '+Fore.LIGHTBLUE_EX+'4')
        print(Fore.WHITE+'Número de cifras: '+Fore.LIGHTBLUE_EX+'5')
        print(Fore.WHITE+'Numeros Repetibles: '+Fore.LIGHTBLUE_EX+'No')
        print(Fore.MAGENTA+'\n2.- '+Fore.LIGHTYELLOW_EX+'Medio'+Fore.WHITE+':')
        print(Fore.WHITE+'Longitud de la contraseña: '+Fore.LIGHTBLUE_EX+'6')
        print(Fore.WHITE+'Número de cifras: '+Fore.LIGHTBLUE_EX+'7')
        print(Fore.WHITE+'Numeros Repetibles: '+Fore.LIGHTBLUE_EX+'No')
        print(Fore.MAGENTA+'\n3.- '+Fore.RED+'Difícil'+Fore.WHITE+':')
        print(Fore.WHITE+'Longitud de la contraseña: '+Fore.LIGHTBLUE_EX+'8')
        print(Fore.WHITE+'Número de cifras: '+Fore.LIGHTBLUE_EX+'9')
        print(Fore.WHITE+'Numeros Repetibles: '+Fore.LIGHTBLUE_EX+'Si'+Style.RESET_ALL)
        
        dif=int(input('\nSelecciona una dificultad: '))         # Leemos la dificultad que ha seleccionado.
        
        while dif!=1 and dif!=2 and dif!=3:             # Comprobación de que es un número válido.
            print(Fore.RED+'¡La opción que has introducido no es válida!'+Style.RESET_ALL)
            dif=int(input('\nSelecciona una dificultad: '))
            
        if dif==1:
            dificultad='facil'          # Dependiendo de la dificultad seleccionada le asignamos a unas variables su longitud y su nombre para usarlas luego.
            longitud=4
        elif dif==2:
            dificultad='medio'
            longitud=6
        else:
            dificultad='dificil'
            longitud=8
            
    elif m1==3:
        # Instrucciones
        print('\U0001F4CB INSTRUCCIONES \U0001F4CB')        
        print('1º- Selecciona una dificultad desde el menú en el apartado de Ajustes.')         # Instrucciones simples del juego
        print('2º- Selecciona Jugar en el menú para iniciar la partida.')
        print('3º- El juego generará una contraseña aleatoria dentro de los parámetros preestablecidos y elegidos.')
        print('4º- Introduce números dentro del rango correspondiente hasta acertar el número.')
        print('Recuerda que tienes una serie de pistas que te ayudarán a encontrar la contraseña.')
        ñ=input('Presiona ENTER para continuar: ')          # Pausamos el código hasta que le de a enter.
        cargando('Saliendo',1)    # Función cargando, especificando que el texto será 'Saliendo' y que se repite una vez.
        
    elif m1==4:     # Opción 4, salir.
        cargando('Saliendo',2)    # Llamamos a la función 'cargando' y le especificamos que queremos que el mensaje sea 'Saliendo' y que me lo repita 2 veces.
        break # Rompemos el bucle
    
    elif m1==1:         # Detectamos si es el inicio del juego.
        contra=[]       # Lista para guardar la contraseña, la ponemos al principio para que se resetee cada vez que se vuelva a jugar.
        contador=0      # Contador de intentos
        print(Fore.BLUE+'Partida Iniciada'+Style.RESET_ALL)         
        
        print(Fore.BLUE+'\nEstás jugando en dificultad:',dd)        # Indicamos al jugador la dificultad en la que está jugando.
        
        print('Pistas:\n Correcto - \U0001F4CC \n Posición no correcta - \U0001F4CD \n No está - \U0000274C')       # Indicamos el funcionamiento de las pistas.
        
        posibilidades=longitud+1    # Usamos la longitud máxima de la contraseña y le sumamos 1 para obtener todos los números posibles.
        if dificultad=='facil' or dificultad=='medio':      # Comprobamos que dificultad es para generar la contraseña. En este caso si es fácil/medio no se puede repetir ningún número por eso está separado.
            for i in range(longitud):           
                tmp=randint(1,posibilidades)    # Hacemos un bucle para generar la contraseña, los números generados se meten en una variable temporal para comprobar si ya está en la lista.
                while True:
                    if tmp not in contra:       # Comprobamos si el número generado ya está en la lista, si está, se lanza número aleatorio hasta que salga uno que no está.
                        contra.append(tmp)
                        break
                    else:
                        tmp=randint(1,posibilidades)
        else:
            for i in range(longitud):                   # Este else, es para la dificultad difícil que se puede repetir el número.
                tmp=randint(1,posibilidades)
                contra.append(tmp)
        #print(Fore.RED,'Contraseña generada aleatoriamente',contra,'Solo para comprobaciones, no estará en la ejecución normal.',Style.RESET_ALL)   #############  Descomentar para mostrar contraseña.
        
        juego=True          # Ponemos la variable juego en True para que cada vez que iniciemos el juego entre.
        
        while juego:        # Iniciamos la recolecta de datos y los tratamos.
            lJugada=[]      # Lista para almacenar la contraseña de los usuarios en una lista.
            jug=''          # Creamos una variable string en blanco para guardar la contraseña del usuario en una cadena.
            jugada=input('Introduce tú número (Longitud: '+ str(longitud)+'): ')               # Separar la combinación y de paso meter un contra
            for i in jugada:
                lJugada.append(int(i))      # Separamos la contraseña y la añadimos dígito a dígito a la lista
                jug+=str(i).ljust(3,' ')    # Lo mismo que antes pero a una cadena y con espacio
            while len(jugada) != len(contra):   # Comprobando si es correcta la longitud
                lJugada=[] # Volvemos a declarar las listas y variables para que queden vacias.
                jug=''
                print(Fore.RED+'La contraseña introducida no tiene la longitud correcta!'+Style.RESET_ALL)
                print(Fore.RED+'Longitud introducida:',Fore.MAGENTA,len(jugada),Fore.RED,'Longitud Correcta:',Fore.LIGHTGREEN_EX,longitud,Style.RESET_ALL)
                jugada=input('Introduce tú número (Longitud: '+ str(longitud)+'): ')
                for i in jugada:
                    lJugada.append(int(i))
                    jug+=str(i).ljust(3,' ')
            contador+=1    # Añadimos un intento al contador
            if lJugada == contra:       # Comprobamos si la jugada del usuario es la misma que la contraseña generada.
                print(Fore.LIGHTGREEN_EX+'\U00002728¡HAS GANADO!\U0001F389'+Style.RESET_ALL)    # Anunciamos que ha ganado
                sleep(.5)
                if contador<3:      # Comprobamos el número de intentos, dependiendo del número de intentos, tendrá un color y un símbolo diferente.
                    print('\U0001F525 Número de intentos:',Fore.GREEN,contador,Style.RESET_ALL,'\U0001F525')    # Color verde y símbolo de llama -- < 3 fallos
                elif contador<6:
                    print('\U000026A1 Número de intentos:',Fore.YELLOW,contador,Style.RESET_ALL,'\U000026A1')   # Color amarillo y símbolo de rayo -- < 6 fallos
                else:
                    print('\U00002744 Número de intentos:',Fore.RED,contador,Style.RESET_ALL,'\U00002744')      # Color rojo y símbolo de copo de nieve -- > 6 fallos
                ñ=input('Presiona ENTER para continuar: ')      # La ejecución se para hasta que se presione enter.
                break   # Rompemos el bucle y volvemos al menú principal
            else:       # Si no es igual, vamos a poner las pistas.
                cadena=''   # Generamos una cadena para almacenar las pistas
                for i in range(len(lJugada)):       
                    if lJugada[i] == contra[i]:
                        cadena+='\U0001F4CC '.ljust(1,' ')      # Si el número coincide se le pone el emoji correspondiente
                    elif lJugada[i] not in contra:
                        cadena+='\U0000274C '.ljust(1,' ')      # Si el número no está en la lista, se le pone el emoji correspondiente
                    else:
                        cadena+='\U0001F4CD '.ljust(1,' ')      # Si el número está en la contraseña pero no en la posición correcta, se le pone el emoji correspondiente
                        
                print('Tú jugada: ',jug)        # Se imprime la jugada del ususario
                print('Tus pistas:',cadena)     # Se imprimen las pistas
                print(Fore.YELLOW+'Número de intentos'.rjust(50,' ')+Fore.CYAN,contador,Style.RESET_ALL)        # Se imprime el contador de fallos
                print(Fore.YELLOW+'Nombre de usuario:'.rjust(50,' ')+Fore.LIGHTBLUE_EX,nombre,Style.RESET_ALL)  # se imprime el nombre de usuario
        cargando('Saliendo',2)      # Llamamos a la función cargar

print(Fore.RED+'PROGRAMA FINALIZADO'+ Style.RESET_ALL)  # FIN DE PROGRAMA