'''Sabemos que el día 1970-01-01 fue jueves. Declarar una función que pueda indicar
cuántos jueves han sido el primer día de cada mes desde entonces. La fecha de corte 
debe de poder ser cualquiera. (1 punto)'''

#Meses con 31 dias:
# treinti_uno = [enero, marzo, mayo, julio, agosto, octubre y diciembre]
# treinta = [Abril, junio, septiembre y noviembre]
# veintiocho = [febrero]


from datetime import datetime


año = int(input("Ingrese un año"))

mes = int(input("Ingrese un mes")) 

año_inicial = 1970

def primer_jueves_mes():
    contador = 0
    #Itero sobre cada año, cada mes y evaluo
    #si el dia 1 de ese cada mes cada año es igual a jueves
    #Week day 3 es jueves

    #Recorro desde el año actual al ingresado
    for year in range(año_inicial, año+1):
        #si año es el actual, voy hasta el mes ingresado
        if year == año:
        for month in range (1,mes+1):
            if datetime (year,month,1).weekday() == 3:
                contador+=1
        else:        
        for month in range (1,13):
            if datetime (year,month,1).weekday() == 3:
                contador+=1

    return contador

print(primer_jueves_mes())