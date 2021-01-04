#Librerias
import serial
import csv
import matplotlib.pyplot as plt

#Funciones
def Modo():
    'Retorna el el modo escogido por el usuario, tomar o analizar datos'
    return input("Desea TOMAR(sensor) o ANALIZAR(archivo) datos: ")

def TomarDatos():
    'Establese la conexion y lee los datos enviados por Arduino, deacurdo a los parametros escogidos por el usuario'
    Valores = [ ]
    i = 0

    Arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600) #Se crea el objeto Arduino con los parametros del puerto serie.

    CantDatos = int(input("Ingrese la cantidad de datos que desea tomar: "))
    Intervalo = input("Ingrese el intervalo de tiempo (min) en el que se tomaran los datos: ")
    
    Arduino.write((Intervalo).encode()) #Se envia el intervalo de tiempo al Arduino de manera codificada.

    #Lee los datos provenientes del puerto serie, los decodifica y los almacena en formato lista dentro de una lista.
    while(i < CantDatos):
        Linea = Arduino.readline().decode()
        print(Linea)
        Valores.append(Linea.split())
        i += 1
    Arduino.close()

    print("Fin del siclo de toma de datos...")
    return Valores

def EscribirArchivo(listValores):
    'Abre o crea un archivo .csv, donde se guardan los valores enviados por Arduino'
    Archivo = open("""
    Ingrese el nombre del archivo en el cual se almacenaran los datos,
    En caso, de que el nombre no conisida o no exista el archivo, se creara uno.
    No olvide escrivir la terminacion ".csv"
    Nombre: """, "w")   #Se abre el archivo en modo escritura.
    escribir = csv.writer(Archivo)

    #Se escriben los datos en formato de filas.
    for renglon in listValores:
        escribir.writerow(renglon)
    Archivo.close()

def LeerArchivo():
    'Abre el archivo escogido, recogiendo y clasificando los datos por tipos'
    Hora = [ ]
    Humedad = [ ]
    Temperatura = [ ]
    Valores = [ ]

    Archivo = open(input("""
    Ingrese el nombre del archivo del cual se desea extraer los datos. En caso, de que el nombre no conisida o no exista el archivo, se producira un error.
    No olvide escrivir la terminacion ".csv"
    Nombre: """), "r")  #Se abre el archivo en modo lectura.

    #Extrae los datos del archivo y los almacena en una lista.
    for renglon in csv.reader(Archivo):
        Valores.append(renglon)
    Archivo.close()
    #Separa y almacena los datos segun su tipo.
    for i in Valores:
        for x in i:
            if(i.index(x) == 0):
                Hora.append(float(x))
            elif(i.index(x) == 1):
                Humedad.append(float(x))
            elif(i.index(x) == 2):
                Temperatura.append(float(x))
    print(Hora)
    print(Humedad)
    print(Temperatura)

    return Hora, Humedad, Temperatura

def MaximosMinimos(Humedad, Temperatura):
    'Establece los valores maximos y minimos'
    #Humedad
    H_max = max(Humedad)
    H_min = min(Humedad)
    #Temperatura
    T_max = max(Temperatura)
    T_min = min(Temperatura)

    return H_max, H_min, T_max, T_min

def Graficar(Hora, Humedad, Temperatura):
    'Realiza los graficos correspondientes'
    TituloGrafico = input("Ingrese el titulo del grafico: ")
    #Grafico N°1
    plt.subplot(2, 1, 1)
    plt.plot(Hora, Humedad, color='b')
    plt.xlim(9, 23)
    plt.title(TituloGrafico)
    plt.ylabel('Humedad(%)')
    #Grafico N°2
    plt.subplot(2, 1, 2)
    plt.plot(Hora, Temperatura, color='r')
    plt.xlim(9, 23)
    plt.ylabel('Temperatura(°C)')
    plt.xlabel('Tiempo(hs)')

    ValoresMaximosMinimos = MaximosMinimos(Humedad, Temperatura)
    print("\nHumedad -->" + " Maximo: " + str(ValoresMaximosMinimos[0]) + "  Minimo: " + str(ValoresMaximosMinimos[1]))
    print("\nTemperatura -->" + " Maximo: " + str(ValoresMaximosMinimos[2]) + "    Minimo: " + str(ValoresMaximosMinimos[3]))

    plt.show()

#Bloque principal
ModoSeleccionado = Modo()

if(ModoSeleccionado == 'tomar'):
    
    datos = TomarDatos()  
    EscribirArchivo(datos)
    
elif(ModoSeleccionado == 'analizar'):

    Parametros = LeerArchivo()
    Graficar(Parametros[0], Parametros[1], Parametros[2])
    
else:
    print("Error... Intente nuevamente")
    Modo()
