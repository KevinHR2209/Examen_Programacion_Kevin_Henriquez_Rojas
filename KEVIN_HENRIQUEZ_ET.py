import random #Libreria para poder generar los sueldos aleatorios
import math #Importo libreria para usar el metodo math.prod para multiplicar los valores
import csv #Importo la libreria para poder hacer el csv

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
diccionario_trabajadores={} #Diccionario para guardar trabajadores con sus sueldos
rango_entre_300000_800000={} #Diccionario para guardar los datos del rango correspondiente
rango_entre_800000_2000000={} #Diccionario para guardar los datos del rango correspondiente
rango_entre_2000000_2500000={} #Diccionario para guardar los datos del rango correspondiente
opcion_menu=0 #Opcion para inicializar el menú


def asignar_sueldos(trabajadores): #Función para asignar sueldos, se le da la lista de trabajadores como argumento
    for nombre in trabajadores: #Recorre todos los nombres de la lista de trabajadores
        sueldo_aleatorio=random.randint(300000,2500000) #Se crea una variable que se reiniciará con un valor aleatorio cada vez que se ingrese un nombre
        diccionario_trabajadores[nombre]=sueldo_aleatorio #Se llena un nuevo diccionario con clave el nombre y valor el numero aleatorio generado que representa el sueldo
    print("\nSueldos asignados exitosamente\n")
    return diccionario_trabajadores #Retorna el sueldo de trabajadores para después usarlo

def clasificar_sueldos(diccionario_trabajadores): #Funcion para clasificar los sueldos
    for nombre,sueldo in diccionario_trabajadores.items(): #Leo los dos valores del diccionario
        if 300000 <= sueldo < 800000: #Si el sueldo está en el rango, agrego el nombre del trabajador y el sueldo al diccionario del rango
            rango_entre_300000_800000[nombre]=sueldo
        if 800000 <= sueldo < 2000000: #Si el sueldo está en el rango, agrego el nombre del trabajador y el sueldo al diccionario del rango
            rango_entre_800000_2000000[nombre]=sueldo
        if 2000000 <= sueldo < 2500000: #Si el sueldo está en el rango, agrego el nombre del trabajador y el sueldo al diccionario del rango
            rango_entre_2000000_2500000[nombre]=sueldo
    print(f"\nSueldos menores a $800.000 TOTAL: {len(rango_entre_300000_800000)}") #Con len determinado la longitud del diccionario para saber la cantidad de trabajadores del rango
    print(f"\n{'Nombre empleado':<20} {'Sueldo'}")
    for nombre,sueldo in rango_entre_300000_800000.items():
        print(f"{nombre:<20} ${sueldo}") #Imprimo el nombre y el sueldo de cada trabajador del rango
    print(f"\nSueldos entre $800.000 y $2.000.000 TOTAL: {len(rango_entre_800000_2000000)}") #Con len determinado la longitud del diccionario para saber la cantidad de trabajadores del rango
    print(f"\n{'Nombre empleado':<20} {'Sueldo'}") 
    for nombre,sueldo in rango_entre_800000_2000000.items():
        print(f"{nombre:<20} ${sueldo}")  #Imprimo el nombre y el sueldo de cada trabajador del rango
    print(f"\nSueldos superioes a $2.000.000 TOTAL: {len(rango_entre_2000000_2500000)}") #Con len determinado la longitud del diccionario para saber la cantidad de trabajadores del rango
    print(f"\n{'Nombre empleado':<20} Sueldo")
    for nombre,sueldo in rango_entre_2000000_2500000.items():
        print(f"{nombre:<20} ${sueldo}") #Imprimo el nombre y el sueldo de cada trabajador del rango
    total_sueldos=0 #Inicializo la variable para poder sacar el total de sueldos
    for sueldo in diccionario_trabajadores.values(): #Leo todos los valores del diccionario
        total_sueldos+=sueldo #Realizo la sumatoria de todos los valores
    print(f"\nTOTAL SUELDOS: ${total_sueldos}\n") #Imprimo el resultado por pantalla
        
def ver_estadisticas(diccionario_trabajadores): #Funcion para que de las estadisticas pedidas
    for nombre,sueldo in diccionario_trabajadores.items(): #Leo todos los nombres y sueldos de los trabajadores
        if sueldo == max(diccionario_trabajadores.values()): #Hago la comparación de si el sueldo es el numero mas alto del diccionario, de ser asi guardo el nombre y el valor para despues imprimirlo
            print(f"\nEl sueldo más alto es ${sueldo} y es del trabajador {nombre}")
    for nombre,sueldo in diccionario_trabajadores.items(): #Leo todos los nombres y sueldos de los trabajadores
        if sueldo == min(diccionario_trabajadores.values()): #Hago la comparación de si el sueldo es el numero mas bajo del diccionario, de ser asi guardo el nombre y el valor para despues imprimirlo
            print(f"El sueldo más bajo es ${sueldo} y es del trabajador {nombre}")
    promedio_sueldos=0 #Inicializo la variable para poder sacar el promedio
    for sueldo in diccionario_trabajadores.values(): #Leo todos los sueldos del diccionario
        promedio_sueldos+=sueldo #Sumo todos los valores para sacar el proomedio
        media_geometrica=math.prod(diccionario_trabajadores.values())**(1/10) #Utilizo el metodo para poder multiplicar todos los valores del diccionario y sacar la raiz decima del producto, lo que corresponde a la media geometrica
    print(f"El promedio de sueldos es ${promedio_sueldos/10}") #Imprimo el promedio de sueldos 
    print(f"La media geométrica es {media_geometrica}\n") #Imprimo la media geometrica

def reporte_sueldos(diccionario_trabajadores,archivo_reporte_csv): #Defino la funcion reporte de sueldos, le doy el diccionario de trabajadores y el archivo_reporte que debe crear
    print(f"\n{'Nombre empleado':<20} {'Sueldo Base':<20} {'Descuento Salud':<20} {'Descuento AFP':<20} {'Sueldo Líquido':<20}") #Con en el :<(numero) doy formato para la impresión 
    for nombre,sueldo in diccionario_trabajadores.items(): #Leo los nombres y valores del diccionario de trabajadores
        salud=sueldo*0.07 #Calculo el descuento de salud
        afp=sueldo*0.12 #Calculo el descuento de afp
        liquido=sueldo-afp-salud #Calculo el sueldo liquido
        print(f"{nombre:<20} ${sueldo:<19} ${salud:<19} ${afp:<19} ${liquido}") #Doy formato a las variables que se van a imprimir por cada trabajador
    with open(archivo_reporte_csv,mode='w',newline='') as archivo: #Abri el archivo, doy el modo de escritura y la estructura para cada linea)
        escribir_reporte=csv.writer(archivo) #Inicio una variable para poder hacer el archivo csv
        escribir_reporte.writerow(['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Líquido']) #Doy el nombre de la primera fila del csv, lo que va a corresponder a los encabezados de la tabla
        for nombre,sueldo in diccionario_trabajadores.items(): #Leo los nombres y valores de los trabajadores
            salud=sueldo*0.07 #Calculo descuento salud
            afp=sueldo*0.12 #Calculo descuento afp
            liquido=sueldo-afp-salud #Calculo sueldo liquido
            escribir_reporte.writerow([nombre,sueldo,salud,afp,liquido]) #Uso la variable del inicio para que cada vez que lea un nombre y sueldo, calcule los descuentos escriba en el archivo las variables nombre,sueldo,salud,afp y liquido
ruta_reporte="archivo_reporte.csv" #Parametro que se la da a la funcion para crear el archivo csv


while opcion_menu !=5:
    try:
        print("\n1. Asignar Sueldos Aleatorios")
        print("2. Clasificar Sueldos")
        print("3. Ver Estadísticas")
        print("4. Reporte de Sueldos")
        print("5. Salir del programa\n")
        opcion_menu=int(input("Ingrese la opción que desea consultar: "))
        if opcion_menu <1 or opcion_menu >5: #Se utiliza para asegurarse de que en caso que ingrtese un numero que no es valido se vuelva a pedir una opcion
            print("Debe ingresar un número entero entre el 1 y el 5")
        match opcion_menu:
            case 1:
                diccionario_trabajadores=asignar_sueldos(trabajadores) #Invoco a la primera funciona
            case 2:
                clasificar_sueldos(diccionario_trabajadores) #Invoco a la segunda funciona
            case 3:
                ver_estadisticas(diccionario_trabajadores) #Invoco a la tercera funciona
            case 4:
                reporte_sueldos(diccionario_trabajadores,ruta_reporte) #Invoco a la cuarta funciona
            case 5:
                print("Finalizando programa...")
                print("Desarrollado por Kevin Henríquez")
                print("RUT 19.327.782 - 9")
                break #Creo la salida de mi codigo
    except UnboundLocalError: #Manejo este error en caso de que se inicialize una opcion que no sea la 1 como primera opcion
        print("Primero debe ejecutar la Opción 1")
    except ValueError: #Manejo este error en caso de que coloquen una opcion que no corresponda a un entero
        print("Debe ingresar un número entero entre el 1 y el 5") 


