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
        '1': ('1.indicar mayor y menor ', accion1),
        '2': ('2.  ingresar tres valores e indicar cual es el mayor', accion2),
        '3': ('3. ingresar tres valores e indicar si es multiplo de 7', accion3),
        '4': ('4.Solicitar el ingreso de tres números mostrar el promedio e indicar si este es par o impar. ', accion4),
        '5': ('5. indicar el total de una telefonia', accion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '7')


def accion1():
    print('Has elegido la opción 1')
    num1=int(input("Ingrese un numero: "));
    num2=int(input("Ingrese otro numero: "));
    if num1 >=  num2 :
     print("el numero mayor es el primero");
    else:
     print("el numero mayor es el segundo");
     if num1 <=  num2 :
      print("el numero menor es el primero");
     else  :
      print("el numero menor es el segundo");



def accion2():
    print('Has elegido la opción 1')
    num1 = int(input("Ingrese un numero: "));
    num2 = int(input("Ingrese otro numero: "));
    num3 = int(input("Ingrese otro numero: "));
    if num1 >= num2:
        print("el numero mayor es el primero");
    elif num2 >= num3:
        print("el numero mayor es el segundo");
    elif num3 >= num1:
            print("el numero mayor es el tercero");







def accion3():
    print('Has elegido la opción 3')
    n4 = int(input("Ingrese un numero: "));
    n5 = int(input("Ingrese un segundo numero  : "));
    n6 = int(input("Ingrese un tercer numero :"));
    suma =int(n4 + n5 + n6) ;
    print("La suma es :", float(suma));
    if suma % 7 ==0:
        print("La suma es multiplo de 7");
    else:

        print("La suma no  es  multiplo de 7");
def accion4():
    print('Has elegido la opción 4')
    n4 = int(input("Ingrese un numero: "));
    n5 = int(input("Ingrese un segundo numero  : "));
    n6 = int(input("Ingrese un tercer numero :"));
    promedio =(n4 + n5 + n6) / 3;
    print("El promedio es :", float(promedio));
    if (promedio %2 == 0):
         print("El promedio es par");
    else :
         print("El promedio es impar");

def accion5():
     print('Has elegido la opción 5')
     nombre = str(input("Ingrese su nombre: "));
     nac = int(input("Los minutos nacionales consumidos fueron: "));
     inter = int(input("Los minutos internacionales consumidos fueron: "));
     total = int(nac + inter);
     if (total > 25):
         if (nac > 25):
             nac -= 25;
             pago = float((nac * 0.5) + (inter * 2.5));
             print(nombre, "tu monto de pago mensual ascinde a: Q", pago);
         else:
             resto = 25 - nac;
             inter -= resto;
             pago = float(inter * 2.5);
             print(nombre, " tu monto de pago mensual ascinde a: Q", pago);
     else:
         print(nombre, " tus minutos son gratis!!");


def salir():

    print('Saliendo')


if __name__ == '__main__':
    menu_principal()






