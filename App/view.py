"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(type,loadfactor):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(type,loadfactor)
    return control



def print_menu():
    print("Bienvenido")
    print("1- Iniciar catalogo")
    print("2- Cargar información")
    print("3- Ejecutar Requerimiento 1")
    print("4- Ejecutar Requerimiento 2")
    print("5- Ejecutar Requerimiento 3")
    print("6- Ejecutar Requerimiento 4")
    print("7- Ejecutar Requerimiento 5")
    print("8- Ejecutar Requerimiento 6")
    print("9- Ejecutar Requerimiento 7")
    print("0- Salir")

def initdatastructs():
    return controller.initdatastructs()
def load_data(data_structs,size):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    controller.load_data(data_structs,size)


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control,year,codigo):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    data = controller.req_1(control,year,codigo)
    print(str(data[0]) + " seg" + " / " + str(data[1]) + " kb")
    data = data[2]
    print(tabulate(data,headers = "firstrow",tablefmt="fancy_grid"))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control,year):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    data = controller.req_3(control,year)
    print(str(data[0]) + " seg" + " / " + str(data[1]) + " kb")
    data = data[2]
    datasector = data[0]
    dataacti = data[1]
    print(tabulate(datasector,headers="firstrow",tablefmt="fancy_grid"))
    print(tabulate(dataacti,headers="firstrow",tablefmt="fancy_grid"))


def print_req_4(control,year):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    data = controller.req_4(control,year)
    print(str(data[0]) + " seg" + " / " + str(data[1]) + " kb")
    data = data[2]
    datasector = data[0]
    dataacti = data[1]
    print(tabulate(datasector,headers="firstrow",tablefmt="fancy_grid"))
    print(tabulate(dataacti,headers="firstrow",tablefmt="fancy_grid"))
    
def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    # TODO: Imprimir el resultado del requerimiento 6
    obj = control[0]
    print(control)
    '''
    data = [("Código sector económico", obj["Código sector económico"]),
    ("Nombre sector económico", obj["Nombre sector económico"]),
    ("Total ingresos netos", obj["Total ingresos netos"]),
    ("Total de costos y gastos", obj["Total de costos y gastos"]),
    ("Total saldo por pagar", obj["Total saldo por pagar"]),
    ("Total saldo a favor", obj["Total saldo a favor"])]

    data1 = [("Código subsector económico Mayor", obj["Subsector Economico Mayor"]["Código subsector económico"]),
    ("Nombre subsector económico", obj["Subsector Economico Mayor"]["Nombre subsector económico"]),
    ("Total ingresos netos", obj["Subsector Economico Mayor"]["Total ingresos netos"]),
    ("Total de costos y gastos", obj["Subsector Economico Mayor"]["Total de costos y gastos"]),
    ("Total saldo por pagar", obj["Subsector Economico Mayor"]["Total saldo por pagar"]),
    ("Total saldo a favor", obj["Subsector Economico Mayor"]["Total saldo a favor"])]

    

    tablesectores = tabulate(list(zip(*data)), headers=[""]*len(data), tablefmt="fancy_grid")
    tablesubsectorMayor = tabulate(list(zip(*data1)), headers=[""]*len(data1), tablefmt="fancy_grid")
  
    # Imprimir la tabla
    print('======= Requerimiento No. 6: Encontrar el sector económico con el mayor total de ingresos netos para un año específico ======\n')
    print(tablesectores)
    print('======= Subsector con mayores aportes ======\n')
    print(tablesubsectorMayor)
    print('======= Actividad con mayores aportes ======\n')
    print(control[0]["Subsector Economico Mayor"]["Actividad Económica Mayor"])
    print('======= Actividad con menores aportes ======\n')
    print(control[0]["Subsector Economico Menor"]["Actividad Económica Menor"])
'''

def print_req_7(control,top,anio,codigo):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    data = controller.req_7(control,top,anio,codigo)
    print(str(data[0]) + " seg" + " / " + str(data[1]) + " kb")
    data = data[2]
    print(tabulate(data,headers="firstrow",tablefmt="fancy_grid"))

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer:.3f}")
        
def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False

def printlista(control):
    control = controller.primerosultimos(control)
    return control
    
def OrderTabulate(first, second, third, fourth, fifth, sixth):
    table = [[first["Año"], first["Código actividad económica"], first["Nombre actividad económica"], first["Código sector económico"], first["Nombre sector económico"], first["Código subsector económico"], first["Nombre subsector económico"], first["Total ingresos netos"], first["Total costos y gastos"], first["Total saldo a pagar"], first["Total saldo a favor"]],
             [second["Año"], second["Código actividad económica"], second["Nombre actividad económica"], second["Código sector económico"], second["Nombre sector económico"], second["Código subsector económico"], second["Nombre subsector económico"], second["Total ingresos netos"], second["Total costos y gastos"], second["Total saldo a pagar"], second["Total saldo a favor"]],
             [third["Año"], third["Código actividad económica"], third["Nombre actividad económica"], third["Código sector económico"], third["Nombre sector económico"], third["Código subsector económico"], third["Nombre subsector económico"], third["Total ingresos netos"], third["Total costos y gastos"], third["Total saldo a pagar"], third["Total saldo a favor"]],
             [fourth["Año"], fourth["Código actividad económica"], fourth["Nombre actividad económica"], fourth["Código sector económico"], fourth["Nombre sector económico"], fourth["Código subsector económico"], fourth["Nombre subsector económico"], fourth["Total ingresos netos"], fourth["Total costos y gastos"], fourth["Total saldo a pagar"], fourth["Total saldo a favor"]],
             [fifth["Año"], fifth["Código actividad económica"], fifth["Nombre actividad económica"], fifth["Código sector económico"], fifth["Nombre sector económico"], fifth["Código subsector económico"], fifth["Nombre subsector económico"], fifth["Total ingresos netos"], fifth["Total costos y gastos"], fifth["Total saldo a pagar"], fifth["Total saldo a favor"]],
             [sixth["Año"], sixth["Código actividad económica"], sixth["Nombre actividad económica"], sixth["Código sector económico"], sixth["Nombre sector económico"], sixth["Código subsector económico"], sixth["Nombre subsector económico"], sixth["Total ingresos netos"], sixth["Total costos y gastos"], sixth["Total saldo a pagar"], sixth["Total saldo a favor"]]]
    headers = ["Año", "Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    return (tabulate(table, headers, tablefmt= "pretty"))
# Se crea el controlador asociado a la vista


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                type = input("Que tipo de mapa desea utilizar (PROBING o CHAINING): \n")
                loadfactor = float(input("Que factor de carga desea utilizar (Ingrese un numero): \n"))
                print("Inicializando Catálogo ....")
                control = new_controller(type, loadfactor)
            elif int(inputs) == 2:
                size = input(" Que tamaño de datos desea utilizar(5pct,10pct,20pct,30pct,50pct,80pct,large,small): ")
                print("Cargando información de los archivos ....")
                answer = controller.load_data(control,size ,memflag=True)
                print('Actividades cargadas: ' + str(controller.actsize(control)))
                printLoadDataAnswer(answer)
                list = printlista(control)
                
                #2012
                First2012 = lt.getElement(list, 1)
                Second2012 = lt.getElement(list, 2)
                Third2012 = lt.getElement(list, 3)
                Fourth2012 = lt.getElement(list, 4)
                Fifth2012 = lt.getElement(list, 5)
                Sixth2012 = lt.getElement(list, 6)
                #2013
                First2013 = lt.getElement(list, 7)
                Second2013 = lt.getElement(list, 8)
                Third2013 = lt.getElement(list, 9)
                Fourth2013 = lt.getElement(list, 10)
                Fifth2013 = lt.getElement(list, 11)
                Sixth2013 = lt.getElement(list, 12)
                #2014
                First2014 = lt.getElement(list, 13)
                Second2014 = lt.getElement(list, 14)
                Third2014 = lt.getElement(list, 15)
                Fourth2014 = lt.getElement(list, 16)
                Fifth2014 = lt.getElement(list, 17)
                Sixth2014 = lt.getElement(list, 18)
                #2015
                First2015 = lt.getElement(list, 19)
                Second2015 = lt.getElement(list, 20)
                Third2015 = lt.getElement(list, 21)
                Fourth2015 = lt.getElement(list, 22)
                Fifth2015 = lt.getElement(list, 23)
                Sixth2015 = lt.getElement(list, 24)
                #2016
                First2016 = lt.getElement(list, 25)
                Second2016 = lt.getElement(list, 26)
                Third2016 = lt.getElement(list, 27)
                Fourth2016 = lt.getElement(list, 28)
                Fifth2016 = lt.getElement(list, 29)
                Sixth2016 = lt.getElement(list, 30)
                #2017
                First2017 = lt.getElement(list, 31)
                Second2017 = lt.getElement(list, 32)
                Third2017 = lt.getElement(list, 33)
                Fourth2017 = lt.getElement(list, 34)
                Fifth2017 = lt.getElement(list, 35)
                Sixth2017 = lt.getElement(list, 36)
                #2018
                First2018 = lt.getElement(list, 37)
                Second2018 = lt.getElement(list, 38)
                Third2018 = lt.getElement(list, 39)
                Fourth2018 = lt.getElement(list, 40)
                Fifth2018 = lt.getElement(list, 41)
                Sixth2018 = lt.getElement(list, 42)
                #2019
                First2019 = lt.getElement(list, 43)
                Second2019 = lt.getElement(list, 44)
                Third2019 = lt.getElement(list, 45)
                Fourth2019 = lt.getElement(list, 46)
                Fifth2019 = lt.getElement(list, 47)
                Sixth2019 = lt.getElement(list, 48)
                #2020
                First2020 = lt.getElement(list, 49)
                Second2020 = lt.getElement(list, 50)
                Third2020 = lt.getElement(list, 51)
                Fourth2020 = lt.getElement(list, 52)
                Fifth2020 = lt.getElement(list, 53)
                Sixth2020 = lt.getElement(list, 54)
                
                print(OrderTabulate(First2012, Second2012, Third2012, Fourth2012, Fifth2012, Sixth2012))
                print(OrderTabulate(First2013, Second2013, Third2013, Fourth2013, Fifth2013, Sixth2013))
                print(OrderTabulate(First2014, Second2014, Third2014, Fourth2014, Fifth2014, Sixth2014))
                print(OrderTabulate(First2015, Second2015, Third2015, Fourth2015, Fifth2015, Sixth2015))
                print(OrderTabulate(First2016, Second2016, Third2016, Fourth2016, Fifth2016, Sixth2016))
                print(OrderTabulate(First2017, Second2017, Third2017, Fourth2017, Fifth2017, Sixth2017))
                print(OrderTabulate(First2018, Second2018, Third2018, Fourth2018, Fifth2018, Sixth2018))
                print(OrderTabulate(First2019, Second2019, Third2019, Fourth2019, Fifth2019, Sixth2019))
                print(OrderTabulate(First2020, Second2020, Third2020, Fourth2020, Fifth2020, Sixth2020))
               
            elif int(inputs) == 3:
                year = input("Para que año desea consultar la actividad con mayor saldo a pagar: ")
                codigo = input("Para que sector desea conocer la actividad con mayor saldo a pagar: ")
                print_req_1(control,int(year),int(codigo))

            elif int(inputs) == 4:
                print_req_2(control)

            elif int(inputs) == 5:
                year = input("Para que año desea consultar el subsector con menores retenciones: ")
                print(print_req_3(control,int(year)))

            elif int(inputs) == 6:
                year = input("Para que año desea consultar el subsector con mayores gastos y costos nomina: ")
                print(print_req_4(control,int(year)))

            elif int(inputs) == 7:
                print_req_5(control)

            elif int(inputs) == 8:
                number = input("Ingrese el año: ")
                answer = controller.req_6(control, int(number), memflag=True)
                print_req_6(answer)  
                

            elif int(inputs) == 9:
                top = int(input("Ingrese el top N de actividades que desea conocer: "))
                anio = int(input("Para que año desea conocer el top " + str(top) +" : " ))
                codigo = int(input("Ingrese el codigo del subsector económico para el que desea conocer el top " + str(top) + ": "))
                print("El top " +str(top) + " de actividades económicas con menores costos y gastos totales para el subsector" + str(codigo) + " en el año" + str(anio) + " es:" )
                print_req_7(control,top,anio,codigo)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
