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
            return '\nDatos invalidos, prueba de nuevo.'
        
        if opcion != 1:
            print("\nSaliendo del programa...")
            ejecucion = False
            
        elif opcion == 1:
            print('\nPassword:')
            generador_contrasenas()
            break
        
        else:
            print("\nOpcion invalida")
            
iniciar_programa()