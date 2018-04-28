print("calculadora")
print("Selecciona una opcion")
opcion=int(input("\n1=suma: \n2=Resta: \n3=Multiplicacion: \n4=Division: \n5=Comparacion de 3 numeros: \n6=IVA: \n7=Tablas de multiplicar \n8=salir"))

if opcion==1:
    a=int(input("Elige un numero"))
    b=int(input("elige otro numero"))
    resultado=(a+b)
    print("El resulatdo de tu suma es: ",resultado)
input("...............")

if opcion==2:
    a=int(input("Escribe tu perimer numero: "))
    b=int(input("Escribe tu segundo numero: "))
    resulatdo=(a-b)
    print("El resultado de tu resta es: ",resultado)
input(".............")

if opcion==3:
    a=int(input("Escribe tu perimer numero: "))
    b=int(input("Escribe tu segundo numero: "))
    resultado=(a*b)
    print("El resultado de tu multiplicacion es: ",resultado)
input(".............")

if opcion==4:
    a=int(input("Escribe tu perimer numero: "))
    b=int(input("Escribe tu segundo numero: "))
    resultado=(a/b)
    print("El resultado de tu division  es: ",resultado)

if opcion==5:
    a=int(input("Dame el valor del numero a:"))
    b=int(input("Dame el valor del numero b:"))
    c=int(input("Dame el valor del numero c:"))
    input("Da enter para evaluar la comparacion")

    if a==b and a==c:
        print("Son iguales")
    if a<b and a<c:
        print("A es mayor")
    if a>b and a>c:
        print("B es mayor")
if opcion==6:
    num1=float(input("ingresa el iva: $"))
    num2=float(input("ingresa la cantidad: $"))
    resultado= num1*num2
    print("El resultado es:",resultado)
    input("Presione cualquier tecla para continuar........")
if opcion==7:
    a=int(input("Escoge la tabla que deseas aprender: "))
    b=int(input("Escoge el rango a multiplicar"))
    for var in range(1,b+1):
        print(var,"x",a,"=",var*a)
if opcion==8:
    print("Gracias por utilizar este programa")
