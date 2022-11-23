def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': (' mostrar la tabla', accion1),
        '2': ('lista de impares', accion2),
        '3': ('numeros multiplos', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('Has elegido la opción 1')
    n = int(input("Ingrese un numero entero: "));
    if n < 0:
            n *= -1;
    inicio=int(input("Ingrese un primer numero "));
    final=int(input("Ingrese un ultimo numero "));
    print("###La tabla es  ",n,"###");
    for i in range (inicio,final+1):
      print(n," * ",i," = ", n*i)

def accion2():
    print('Has elegido la opción 2')

    x =int(input("ingrese un valor"))
    print("la lista de impares son las siguentes")

    for i in range(1,x,2):
        print(i)






def accion3():
    print('Has elegido la opción 3')
    j=int(input("ingrese un numero"))
    if (j<0):
      j*=-1;
    print("los muntiplos son: ",j," 1 al 100")
    for i in range (1,100):
        if(i% j==0):
            print(i);







def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()







