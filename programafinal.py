print("Ingresa el la operacion que quieres realizar")

opcion=int(input("0=Comparacion: \n1=suma:\n2=Resta:\n3=Multiplicacion:\n4=Datos de usuario:\n5=Division:\n6=tablas de ,multiplicar:\n7=finalizar el programa:"))

if opcion==0:
    a=int(input("Dame el valor del numero a:"))
    b=int(input("Dame el valor del numero b:"))
    input("Da enter para evaluar la comparacion")

    if a==b:
        print("Son iguales")
    if a<b:
        print("A es mayor")
    if a>b:
        print("B es mayor")
    print("Esta lista tu comparacion :)")
    input(".........")
elif opcion==1:
    a=int(input("ingrese el numero A:"))
    b=int(input("ingresa el numero B:"))
    resultado=(a+b)
    print("el resulado de la suma es?",resultado)
    input(".........")
elif opcion==2:
    a=int(input("ingrese el primer numero a restar:"))
    b=int(input("Ingrese el segundo numero a restar"))
    resultado=(a-b)
    print("El resultado de tu resta es:",resulado)
    input(".........")
elif opcion==3:
    a=int(input("Ingrese el primer numero a multiplicar:"))
    b=int(input("Ingrese el segundo numero  a multiplicar:"))
    resultado=(a*b)
    print("El resultado de tu multiplicacion es:",resultado)
elif opcion==4:
    nombre=input("Tu nombre es:")
    edad=int(input("Tu edad es de:"))
    peso=float(input("Tu peso es de:"))
    estatura=float(input("Tu estatura es de:"))
    print("Hola",nombre,"tienes",edad,"años","con un peso de:",peso,"kg","Y una estatura de:",Estatura)
elif opcion==5:
    a=int(input("Ingresa el primer valor a dividir:"))
    b=int(input("Ingresa el segundo dato a dividir:"))
    resultado=(a/b)
    print("Tu resultado es:",resultado)
elif opcion==6:
    a=int(input("Escoge la tabla que deseas aprender: "))
    b=int(input("Escoge el rango a multiplicar"))
    for var in range(1,b+1):
        print(var,"x",a,"=",var*a)

input(".............")
if opcion==7:
    print("gracias por usar este preograma :) adios...")

input("..............")
