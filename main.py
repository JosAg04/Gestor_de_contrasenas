import random
import string

# Menu de inicio

def menu():
    
    print('''
        ======================
             MENU INICIAL
        ======================
          1-Crear contrasena
          2-Salir
        ======================
          ''')

def generador_contrasenas():
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    chars = lower + upper + num + symbols

    temp = random.sample(chars, 25)
    print("".join(temp))
    
def iniciar_programa():
    
    ejecucion = True
    
    while ejecucion:
        
        menu()
        
        try:
            
            opcion = int(input('\nElige una opcion: '))
            
        except (ValueError, KeyboardInterrupt):
            print('\nDatos invalidos, prueba de nuevo.')
            continue
        
        if opcion == 1:
            print('\nPassword:')
            generador_contrasenas()
            
        elif opcion == 2:
            print("\nSaliendo del programa...")
            ejecucion = False
            
        else:
            print("\nOpcion invalida, intenta con 1 o 2")
            
iniciar_programa()