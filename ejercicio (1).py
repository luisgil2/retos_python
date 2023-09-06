

resultado = 0.00
tiempo = int(input("introduzca las horas que mantuvo estacionado "))
tiempo2 = int(input("introduzca los minutos que mantuvo estacionado "))
dia = int(input("1. Lunes, martes o miercoles, 2. Jueves, viernes, 3. Sabado, domingo "))




if(dia == 1):
    if(tiempo2 >= 5):
        resultado = (tiempo + 1)*2.00
    else:
        resultado = tiempo * 2.00    
elif(dia==2):     
     if(tiempo2 >= 5):
        resultado = (tiempo + 1)*2.50
     else:
        resultado = tiempo * 2.50  
elif(dia==3):
     if(tiempo2 >= 5):
        resultado = (tiempo + 1)*3.00
     else:
        resultado = tiempo * 3.00  
else:
    print("seleccion incorrecta")


print(f"el total a pagar es de: {resultado} dolares")