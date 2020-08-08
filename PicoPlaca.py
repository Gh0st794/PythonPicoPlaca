from datetime import datetime, date, time


def picoPlaca(plateLastDigit, yr, mth, day, h, mn, sec):
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
        if( (plateLastDigit==1 or plateLastDigit==2 and diaIngresado == "Monday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ): 
            circula=False
        elif( (plateLastDigit==3 or plateLastDigit==4 and diaIngresado == "Tuesday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ):
            circula=False
        elif( (plateLastDigit==5 or plateLastDigit==6 and diaIngresado == "Wednesday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ):
            circula=False
        elif( (plateLastDigit==7 or plateLastDigit==8 and diaIngresado == "Thursday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ):
            circula=False
        elif( (plateLastDigit==9 or plateLastDigit==0 and diaIngresado == "Friday") or (horaIngresada>=horaAm1 and horaIngresada<=horaAm2) or (horaIngresada>=horaPm1 and horaIngresada<=horaPm2) ):
            circula=False

    return circula


print("\tPICO Y PLACA-PREDICTOR")

flag=True
while(flag==True):
    placa=input("Ingrese la placa de su vehículo(AAA-0123):")   
    try:
        lastDigit=int(placa[len(placa)-1])        
        flag=False     
    except:
        print("Placa no valida")
        continue

print('Placa ingresada: ',placa.upper())
print('Ultimo digito: ',lastDigit)


flag=True
while(flag==True):
    fecha=input("Ingrese la fecha (dd/mm/yyyy):")
    for f in fecha:
        if f=='/':
            nuevaFecha=fecha.split('/')        
        else:
            if f=='-':
                nuevaFecha=fecha.split('-')
            else:
                nuevaFecha=fecha.split()
    try:        
        dia=int(nuevaFecha[0]) 
        mes=int(nuevaFecha[1])
        year=int(nuevaFecha[2])
        fechaIng=date(year, mes, dia)
        flag=False     
    except:
        print("Fecha no valida")
        continue

print('Fecha ingresada: ',fechaIng)

flag=True
while(flag==True):
    Hora=input("Ingrese la hora(hh:mm:ss):")
    if f==':':        
        nuevaHora=Hora.split(':')
    else:
        nuevaHora=Hora.split()

    try:
        Hora=int(nuevaHora[0])
        minuto=int(nuevaHora[1])
        segundo=int(nuevaHora[2])
        horaIng=time(Hora, minuto, segundo)
        flag=False
    except:
        print("Hora no valida")
        continue

print('Hora ingresada: ', horaIng)
fechaHora=datetime(year, mes, dia, Hora, minuto, segundo)
print('Fecha final: ', fechaHora.strftime("%c"))
print(fechaHora.strftime("%A"))

if( picoPlaca(lastDigit, year, mes, dia, Hora, minuto, segundo) == True ):
    print("Usted si puede circular")
else:
    print("Usted no puede circular")




