from datetime import datetime, date, time


def picoPlaca(placaUltimoDigito, yr, mth, day, h, mn, sec):
    circula=True
    fechaHora=datetime(yr, mth, day, h, mn, sec)    
    horaAm1=time(7,00,00)
    horaAm2=time(9,30,00)
    horaPm1=time(16,00,00)
    horaPm2=time(19,30,00)
    horaIngresada=time(h,mn,sec)
    diaIngresado = fechaHora.strftime("%A")
    
    if(diaIngresado == "Saturday" or diaIngresado == "Sunday"):
        circula=True
    else:
        if( (placaUltimoDigito==1 or placaUltimoDigito==2 and diaIngresado == "Monday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ): 
            circula=False
        elif( (placaUltimoDigito==3 or placaUltimoDigito==4 and diaIngresado == "Tuesday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ):
            circula=False
        elif( (placaUltimoDigito==5 or placaUltimoDigito==6 and diaIngresado == "Wednesday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ):
            circula=False
        elif( (placaUltimoDigito==7 or placaUltimoDigito==8 and diaIngresado == "Thursday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ):
            circula=False
        elif( (placaUltimoDigito==9 or placaUltimoDigito==0 and diaIngresado == "Friday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ):
            circula=False

    return circula

def validarPlaca(placa):
    
    if( (len(placa)<7) or len(placa)>8 ):
        return False

    try:
        nuevaPlaca=placa.split("-")
    except:      
        return False
        
    letras=nuevaPlaca[0]
    if( letras.isalpha() and len(letras)>0 and len(letras)==3 ):
        l=str(letras)
    else:
        return False
        
    numeros=nuevaPlaca[1]
    if( numeros.isdigit() and len(numeros)>0 and (len(numeros)==4 or len(numeros)==3 ) ):
        n=int(numeros)
    else:
        return False
            
    if( l.isalpha() and type(n)==int):      
        return True            
    else:
        return False


print("\tPICO Y PLACA-PREDICTOR")

flag=True
while(flag==True):
    placa=input('Ingrese la placa de su vehículo(AAA-0123):')
    if( validarPlaca(placa) == True ):
        flag=False
    else:
        print("Placa no valida")
        flag=True

ultimoDigito=int(placa[len(placa)-1])
print('Placa ingresada: ',placa.upper())
print('Ultimo digito: ',ultimoDigito)

flag=True
while(flag==True):
    fecha=input('Ingrese la fecha (dd/mm/yyyy):')
    try:
        nuevaFecha=fecha.split("/")
        dia=int(nuevaFecha[0])
        mes=int(nuevaFecha[1])
        year=int(nuevaFecha[2])
        fechaIng=date(year, mes, dia)
        flag=False
    except:
        print('Fecha no valida')
        continue

print('Fecha ingresada: ',fechaIng)

flag=True
while(flag==True):
    Hora=input('Ingrese la hora(hh:mm:ss):')    
    try:
        nuevaHora=Hora.split(":")
        hora=int(nuevaHora[0])
        minuto=int(nuevaHora[1])
        segundo=int(nuevaHora[2])
        horaIng=time(hora, minuto, segundo)
        flag=False
    except:
        print('Hora no valida')
        continue

print('Hora ingresada: ', horaIng)
fechaHora=datetime(year, mes, dia, hora, minuto, segundo)
print('Fecha final: ', fechaHora.strftime("%c"))
print(fechaHora.strftime("%A"))

if( picoPlaca(ultimoDigito, year, mes, dia, hora, minuto, segundo) == True ):
    print("Usted si puede circular")
else:
    print("Usted no puede circular")