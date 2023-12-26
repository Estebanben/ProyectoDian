"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(type,loadfactor):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {"actividades":None,
                    "anios":None}

    data_structs["actividades"] = lt.newList("ARRAY_LIST",Comparecodigo)
    
    data_structs["anios"] = mp.newMap(40,maptype=type,loadfactor=loadfactor,cmpfunction = compareMapYear)
    return data_structs
# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    try:
        years = data_structs['anios']
        if (data['Año'] != ''):
            pubyear = data['Año']
            pubyear = int(float(pubyear))
        else:
            pubyear = 2020
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = new_data(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year['actividades'], data)
    except Exception:
        return None
def add_data_subsec(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    try:
        years = data_structs
        if (data['Código subsector económico'] != ''):
            subcod = data['Código subsector económico']
            subcod = int(float(subcod))
        else:
            subcod = 20
        existyear = mp.contains(years, subcod)
        if existyear:
            entry = mp.get(years, subcod)
            year = me.getValue(entry)
        else:
            year = new_data(subcod)
            mp.put(years, subcod, year)
        lt.addLast(year['actividades'], data)
    except Exception:
        return None

def add_data_sec(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    try:
        years = data_structs
        if (data['Código sector económico'] != ''):
            subcod = data['Código sector económico']
            subcod = int(float(subcod))
        else:
            subcod = 20
        existyear = mp.contains(years, subcod)
        if existyear:
            entry = mp.get(years, subcod)
            year = me.getValue(entry)
        else:
            year = new_data(subcod)
            mp.put(years, subcod, year)
        lt.addLast(year['actividades'], data)
    except Exception:
        return None
    
def add_actividad(data_structs,actividad):
    lt.addLast(data_structs['actividades'],actividad)
    add_data(data_structs,actividad)
    return data_structs

def add_actividad_sub(data_structs,actividad):
    add_data_subsec(data_structs,actividad)
    return data_structs

def add_actividad_sec(data_structs,actividad):
    add_data_sec(data_structs,actividad)
    return data_structs

def new_data(anio):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    entry = {'year': "", "actividades": None}
    entry['year'] = anio
    entry['actividades'] = lt.newList('ARRAY_LIST')
    return entry


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs['actividades'])


def req_1(data_structs,year,codigo):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    listaanio = getactibyYear(data_structs,year)
    
    mapasubsec = mp.newMap(numelements=40,maptype="PROBING",loadfactor=0.5)
    for data in listaanio["elements"]:
        add_actividad_sec(mapasubsec,data)

    actsubsec = mp.get(mapasubsec,int(codigo))
    actsubsec = actsubsec["value"]["actividades"]
    quk.sort(actsubsec,compareSaldop)
    
    actividad = lt.getElement(actsubsec,1)
    headers = ["Código actividad económica","Nombre actividad económica","Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    actividad_tab = []
    actividad_tab.append (actividad["Código actividad económica"])
    actividad_tab.append(actividad["Nombre actividad económica"])
    actividad_tab.append(actividad["Código subsector económico"])
    actividad_tab.append(actividad["Nombre subsector económico"])
    actividad_tab.append(actividad["Total ingresos netos"])
    actividad_tab.append(actividad["Total costos y gastos"]) 
    actividad_tab.append (actividad["Total saldo a pagar"])
    actividad_tab.append(actividad["Total saldo a favor"])
    actividad_tabulate = []
    actividad_tabulate.append(headers)
    actividad_tabulate.append(actividad_tab)
    return actividad_tabulate
    
def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs,year):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    ListaFinalvalores = lt.newList(datastructure="ARRAY_LIST")
    list_anio = getactibyYear(data_structs,year)
    Newlist = lt.newList(datastructure="ARRAY_LIST")
    dict_info = {}
    dict_infoad = {}
    Newlistad = lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(Newlist,dict_info)
    for value in range(lt.size(list_anio)):
            
        sublist = list_anio["elements"][value]
        if sublist["Nombre subsector económico"] not in lt.getElement(Newlist,1):
            codsector = sublist["Código sector económico"]   
            nombresec = sublist["Nombre sector económico"] 
            codsub = sublist["Código subsector económico"]
            tingnet = int(sublist["Total ingresos netos"])
            tcyg = int(sublist["Total costos y gastos"])
            tsaldop = int(sublist["Total saldo a pagar"])
            tsaldof = int(sublist["Total saldo a favor"])
            tcygn = int(sublist["Total retenciones"])
            nombresub = sublist["Nombre subsector económico"]
            
            dict_info[nombresub] = tcygn
            dict_infoad[nombresub + "codsector"] = codsector
            dict_infoad[nombresub + "nombresec"] = nombresec
            dict_infoad[nombresub + "codsub"] = codsub
            dict_infoad[nombresub] = tcygn
            dict_infoad[nombresub + "ingnet"] = tingnet
            dict_infoad[nombresub + "coyga"] = tcyg
            dict_infoad[nombresub + "ttlsaldoP"] = tsaldop
            dict_infoad[nombresub + "ttlsaldoF"] = tsaldof
        else:
            nombresub = sublist["Nombre subsector económico"]
            tcygn = int(lt.getElement(Newlist,1)[nombresub])
            tcynga = int(lt.getElement(Newlistad,1)[nombresub])
            tingnet = int(lt.getElement(Newlistad,1)[nombresub + "ingnet"])
            tcyg = int(lt.getElement(Newlistad,1)[nombresub + "coyga"])
            tsaldop = int(lt.getElement(Newlistad,1)[nombresub + "ttlsaldoP"])
            tsaldof = int(lt.getElement(Newlistad,1)[nombresub + "ttlsaldoF"])
            dict_info[nombresub] = tcygn + int(sublist["Costos y gastos nómina"])
            dict_infoad[nombresub] = tcynga + int(sublist["Total retenciones"])
            dict_infoad[nombresub + "ingnet"] = tingnet + int(sublist["Total ingresos netos"])
            dict_infoad[nombresub + "coyga"] = tcyg + int(sublist["Total costos y gastos"])
            dict_infoad[nombresub + "ttlsaldoP"] = tsaldop + int(sublist["Total saldo a pagar"])
            dict_infoad[nombresub + "ttlsaldoF"] = tsaldof + int(sublist["Total saldo a pagar"])
        lt.addFirst(Newlist, dict_info)
        lt.addFirst(Newlistad,dict_infoad)
            
            # if count < (len(list_2012["elements"])):
            #     lt.removeFirst(Newlist)
    lista_sector = lt.getElement(Newlist,lt.size(Newlist))
    lista_sectorad = lt.getElement(Newlistad,lt.size(Newlistad))
    valores = list(lista_sector.values())
    sectores = list(lista_sector.keys())
    posible_m = valores[1]
    posible_m_s = sectores[1]
    i = 0
    while i < len(valores):
        if valores[i] < posible_m:
            posible_m = valores[i]
            posible_m_s = sectores[i]
            
        i+=1
    
    subcodsec = lista_sectorad[posible_m_s + "codsector"]
    subnombresec = lista_sectorad[posible_m_s + "nombresec"]
    subcod = lista_sectorad[posible_m_s + "codsub"]
    subingresos = lista_sectorad[posible_m_s + "ingnet"]
    subcostosgastos =lista_sectorad[posible_m_s + "coyga"]
    subttlsaldopagar = lista_sectorad[posible_m_s + "ttlsaldoP"]
    subttlsaldofavor = lista_sectorad[posible_m_s + "ttlsaldoF"]
        
        
        
    lt.addLast(ListaFinalvalores,subcodsec)
    lt.addLast(ListaFinalvalores,subnombresec)   
    lt.addLast(ListaFinalvalores,subcod) 
    lt.addLast(ListaFinalvalores,posible_m_s)
    lt.addLast(ListaFinalvalores,posible_m)
    lt.addLast(ListaFinalvalores,subingresos)
    lt.addLast(ListaFinalvalores,subcostosgastos)
    lt.addLast(ListaFinalvalores,subttlsaldopagar)
    lt.addLast(ListaFinalvalores,subttlsaldofavor)
    
    mapasubsec = mp.newMap(numelements=40,maptype="PROBING",loadfactor=0.5)
    for data in list_anio["elements"]:
        add_actividad_sub(mapasubsec,data)
    
    codigo = lt.getElement(ListaFinalvalores,3)
    actsubsec = mp.get(mapasubsec,int(codigo))
    actsubsec = actsubsec["value"]["actividades"]
    quk.sort(actsubsec,compareRetenciones)
    listaaportes = lt.newList("ARRAY_LIST")
    if int(lt.size(actsubsec)) < 6:
        i = 0
        while i < lt.size(actsubsec):
            lt.addLast(listaaportes,lt.getElement(actsubsec,i))
            i+=1
    else:
        lt.addLast(listaaportes,lt.getElement(actsubsec,lt.size(actsubsec)))
        lt.addLast(listaaportes,lt.getElement(actsubsec,(lt.size(actsubsec)-1)))
        lt.addLast(listaaportes,lt.getElement(actsubsec,(lt.size(actsubsec)-2)))
        lt.addLast(listaaportes,lt.getElement(actsubsec,3))
        lt.addLast(listaaportes,lt.getElement(actsubsec,2))
        lt.addLast(listaaportes,lt.getElement(actsubsec,1))
    
    tuplavalores = (ListaFinalvalores,listaaportes)
    
    data1 = tuplavalores[0]
    data2 = tuplavalores[1]
    headers = ["Código actividad económica","Nombre actividad económica","Total retenciones","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    headers2 = ["Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total retenciones","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    tabulatelist1 = []
    tablist2 = []
    tablist2.append(headers)
    for item in data2["elements"]:
        tabulatelist2 = []
        tabulatelist2.append(item["Código actividad económica"])
        tabulatelist2.append(item["Nombre actividad económica"])
        tabulatelist2.append(item["Total retenciones"])
        tabulatelist2.append(item["Total ingresos netos"])
        tabulatelist2.append(item["Total costos y gastos"])
        tabulatelist2.append(item["Total saldo a pagar"])
        tabulatelist2.append(item["Total saldo a favor"])
        tablist2.append(tabulatelist2)
    for item in data1["elements"]:
        tabulatelist1.append(item)
    tablist = []
    tablist.append(headers2)
    tablist.append(tabulatelist1)
    tuplaTabulate = (tablist,tablist2)
    return tuplaTabulate


def req_4(data_structs,year):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    ListaFinalvalores = lt.newList(datastructure="ARRAY_LIST")
    list_anio = getactibyYear(data_structs,year)
    Newlist = lt.newList(datastructure="ARRAY_LIST")
    dict_info = {}
    dict_infoad = {}
    Newlistad = lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(Newlist,dict_info)
    for value in range(lt.size(list_anio)):
            
        sublist = list_anio["elements"][value]
        if sublist["Nombre subsector económico"] not in lt.getElement(Newlist,1):
            codsector = sublist["Código sector económico"]   
            nombresec = sublist["Nombre sector económico"] 
            codsub = sublist["Código subsector económico"]
            tingnet = int(sublist["Total ingresos netos"])
            tcyg = int(sublist["Total costos y gastos"])
            tsaldop = int(sublist["Total saldo a pagar"])
            tsaldof = int(sublist["Total saldo a favor"])
            tcygn = int(sublist["Costos y gastos nómina"])
            nombresub = sublist["Nombre subsector económico"]
            
            dict_info[nombresub] = tcygn
            dict_infoad[nombresub + "codsector"] = codsector
            dict_infoad[nombresub + "nombresec"] = nombresec
            dict_infoad[nombresub + "codsub"] = codsub
            dict_infoad[nombresub] = tcygn
            dict_infoad[nombresub + "ingnet"] = tingnet
            dict_infoad[nombresub + "coyga"] = tcyg
            dict_infoad[nombresub + "ttlsaldoP"] = tsaldop
            dict_infoad[nombresub + "ttlsaldoF"] = tsaldof
        else:
            nombresub = sublist["Nombre subsector económico"]
            tcygn = int(lt.getElement(Newlist,1)[nombresub])
            tcynga = int(lt.getElement(Newlistad,1)[nombresub])
            tingnet = int(lt.getElement(Newlistad,1)[nombresub + "ingnet"])
            tcyg = int(lt.getElement(Newlistad,1)[nombresub + "coyga"])
            tsaldop = int(lt.getElement(Newlistad,1)[nombresub + "ttlsaldoP"])
            tsaldof = int(lt.getElement(Newlistad,1)[nombresub + "ttlsaldoF"])
            dict_info[nombresub] = tcygn + int(sublist["Costos y gastos nómina"])
            dict_infoad[nombresub] = tcynga + int(sublist["Costos y gastos nómina"])
            dict_infoad[nombresub + "ingnet"] = tingnet + int(sublist["Total ingresos netos"])
            dict_infoad[nombresub + "coyga"] = tcyg + int(sublist["Total costos y gastos"])
            dict_infoad[nombresub + "ttlsaldoP"] = tsaldop + int(sublist["Total saldo a pagar"])
            dict_infoad[nombresub + "ttlsaldoF"] = tsaldof + int(sublist["Total saldo a pagar"])
        lt.addFirst(Newlist, dict_info)
        lt.addFirst(Newlistad,dict_infoad)
            
            # if count < (len(list_2012["elements"])):
            #     lt.removeFirst(Newlist)
    lista_sector = lt.getElement(Newlist,lt.size(Newlist))
    lista_sectorad = lt.getElement(Newlistad,lt.size(Newlistad))
    valores = list(lista_sector.values())
    sectores = list(lista_sector.keys())
    posible_m = valores[1]
    posible_m_s = sectores[1]
    i = 0
    while i < len(valores):
        if valores[i] > posible_m:
            posible_m = valores[i]
            posible_m_s = sectores[i]
            
        i+=1
    
    subcodsec = lista_sectorad[posible_m_s + "codsector"]
    subnombresec = lista_sectorad[posible_m_s + "nombresec"]
    subcod = lista_sectorad[posible_m_s + "codsub"]
    subingresos = lista_sectorad[posible_m_s + "ingnet"]
    subcostosgastos =lista_sectorad[posible_m_s + "coyga"]
    subttlsaldopagar = lista_sectorad[posible_m_s + "ttlsaldoP"]
    subttlsaldofavor = lista_sectorad[posible_m_s + "ttlsaldoF"]
        
        
        
    lt.addLast(ListaFinalvalores,subcodsec)
    lt.addLast(ListaFinalvalores,subnombresec)   
    lt.addLast(ListaFinalvalores,subcod) 
    lt.addLast(ListaFinalvalores,posible_m_s)
    lt.addLast(ListaFinalvalores,posible_m)
    lt.addLast(ListaFinalvalores,subingresos)
    lt.addLast(ListaFinalvalores,subcostosgastos)
    lt.addLast(ListaFinalvalores,subttlsaldopagar)
    lt.addLast(ListaFinalvalores,subttlsaldofavor)
    
    mapasubsec = mp.newMap(numelements=40,maptype="PROBING",loadfactor=0.5)
    for data in list_anio["elements"]:
        add_actividad_sub(mapasubsec,data)
    
    codigo = lt.getElement(ListaFinalvalores,3)
    actsubsec = mp.get(mapasubsec,int(codigo))
    actsubsec = actsubsec["value"]["actividades"]
    quk.sort(actsubsec,compareCostoGastoN)
    listaaportes = lt.newList("ARRAY_LIST")
    
    if int(lt.size(actsubsec)) < 6:
        i = 0
        while i < lt.size(actsubsec):
            lt.addLast(listaaportes,lt.getElement(actsubsec,i))
            i+=1
    else:
        lt.addLast(listaaportes,lt.getElement(actsubsec,lt.size(actsubsec)))
        lt.addLast(listaaportes,lt.getElement(actsubsec,(lt.size(actsubsec)-1)))
        lt.addLast(listaaportes,lt.getElement(actsubsec,(lt.size(actsubsec)-2)))
        lt.addLast(listaaportes,lt.getElement(actsubsec,3))
        lt.addLast(listaaportes,lt.getElement(actsubsec,2))
        lt.addLast(listaaportes,lt.getElement(actsubsec,1))
    
    tuplavalores = (ListaFinalvalores,listaaportes)
    
    data1 = tuplavalores[0]
    data2 = tuplavalores[1]
    headers = ["Código actividad económica","Nombre actividad económica","Costos y gastos nómina","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    headers2 = ["Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total costos y gastos nómina","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    tabulatelist1 = []
    tablist2 = []
    tablist2.append(headers)
    for item in data2["elements"]:
        tabulatelist2 = []
        tabulatelist2.append(item["Código actividad económica"])
        tabulatelist2.append(item["Nombre actividad económica"])
        tabulatelist2.append(item["Costos y gastos nómina"])
        tabulatelist2.append(item["Total ingresos netos"])
        tabulatelist2.append(item["Total costos y gastos"])
        tabulatelist2.append(item["Total saldo a pagar"])
        tabulatelist2.append(item["Total saldo a favor"])
        tablist2.append(tabulatelist2)
    for item in data1["elements"]:
        tabulatelist1.append(item)
    tablist = []
    tablist.append(headers2)
    tablist.append(tabulatelist1)
    tuplaTabulate = (tablist,tablist2)
    return tuplaTabulate

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs, year):
    """
    Función que soluciona el requerimiento 6 :
    Encontrar el sector económico con el mayor total de 
    ingresos netos para un año específico 
    """
    #inicia obteniendo la lista completa por el año consultado
    print(year);
    actiByYear  =  getactibyYear(data_structs,year)
    if actiByYear:

        """
        print('Lista encontrada...',actiByYear)
        sorted_list = sa.sort(actiByYear, compareTotalIngresosNetos)
        numele      = actiByYear['size']
        ranked_list = lt.subList(sorted_list, 1,numele)
        print('ranked',ranked_list)

        """
        mayorSector = buscarMayorSectorEconomico(actiByYear)   
        return mayorSector
    else : 
        return None  


def req_7(data_structs,top,anio,codigo):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    datosanio = getactibyYear(data_structs,anio)

    mapasubsec = mp.newMap(numelements=40,maptype="PROBING",loadfactor=0.5)
    for data in datosanio["elements"]:
        add_actividad_sub(mapasubsec,data)
    
    listsubsec = mp.get(mapasubsec,codigo)
    listsubsec = listsubsec["value"]["actividades"]
    
    quk.sort(listsubsec,compareCostosGastos)
    
    i = 1
    listavalores = lt.newList("ARRAY_LIST")
    size = lt.size(listsubsec)
    if int(size) <= int(top): 
        while i <= size:
            lt.addLast(listavalores,lt.getElement(listsubsec,i))
            i += 1
    else:
        while i <= top:
            lt.addLast(listavalores,lt.getElement(listsubsec,i))
            i += 1
    headers = ["Código actividad económica","Nombre actividad económica","Código sector económmico","Nombre sector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]    
    listatab = [] 
    listatab.append(headers)
    for item in listavalores["elements"]:
        temptablist = []
        temptablist.append(item["Código actividad económica"])       
        temptablist.append(item["Nombre actividad económica"])
        temptablist.append(item["Código sector económico"])
        temptablist.append(item["Nombre sector económico"])
        temptablist.append(item["Total ingresos netos"])
        temptablist.append(item["Total costos y gastos"])
        temptablist.append(item["Total saldo a pagar"])
        temptablist.append(item["Total saldo a favor"])
        listatab.append(temptablist)
    return listatab
        
def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

def getactibyYear(data_structs,year):
    year = mp.get(data_structs['anios'], year)
    if year:
        return me.getValue(year)['actividades']
    return None

def primerosultimos(data_strucs):
    anio = 2012
    listapu = lt.newList(datastructure="ARRAY_LIST")
    while anio < 2021:
        listaanio = getactibyYear(data_strucs,anio)
        quk.sort(listaanio,compareCodigoact)
        lt.addLast(listapu,lt.getElement(listaanio,1))
        lt.addLast(listapu,lt.getElement(listaanio,2))
        lt.addLast(listapu,lt.getElement(listaanio,3))
        lt.addLast(listapu,lt.getElement(listaanio,lt.size(listaanio)))
        lt.addLast(listapu,lt.getElement(listaanio,(int(lt.size(listaanio))-1)))
        lt.addLast(listapu,lt.getElement(listaanio,(int(lt.size(listaanio))-2)))
        anio += 1
    return listapu
# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def Comparecodigo(codigo1,codigo2):
    if codigo1 > codigo2:
        return 1
    if codigo1 < codigo2:
        return -1
    if codigo1 == codigo2:
        return 0
    
def compareMapYear(year, actividad):
    actentry = me.getKey(actividad)
    if (year == actentry):
        return 0
    elif (year > actentry):
        return 1
    else:
        return -1
    
def compareCodigoact(data1,data2):
    if data1["Código actividad económica"] > data2["Código actividad económica"]:
        return 1
    else:
        return -1

def compareCostoGastoN(data1,data2):
    return int(data1["Costos y gastos nómina"]) > int(data2["Costos y gastos nómina"])
       
def compareCostosGastos(data1,data2):
    return int(data1["Total costos y gastos"]) < int(data2["Total costos y gastos"])

def compareSaldop(data1,data2):

    return int(data1["Total saldo a pagar"]) > int(data2["Total saldo a pagar"])


def buscarMayorSectorEconomico(datos):

    #print('data',datos)
    # se crea obj sectores 
    sectores = {}
    subsectores = {}
    actividades = {}
    actividadesMenor = {}
    ########### INCIA LOGICA de SECTORES MAYOR############  
    for actividad in datos['elements']:
        #obtener sector por la actividad economica
        codigo_sector = int(actividad['Código sector económico'])
        #pregunta si el sector esta dentro de la lista de sectores si no lo crea
        if codigo_sector not in sectores:
            sectores[codigo_sector] = {
                'Nombre sector económico': actividad['Nombre sector económico'],
                'Total ingresos netos': 0,
                'Total de costos y gastos': 0,
                'Total saldo por pagar': 0,
                'Total saldo a favor': 0,
            }
        #se llena la informacion del sector si ya exsiste le suma los valores
        sector = sectores[codigo_sector]
        sector['Total ingresos netos'] += int(actividad['Total ingresos netos'])
        sector['Total de costos y gastos'] += int(actividad['Total costos y gastos'])
        sector['Total saldo por pagar'] += int(actividad['Total saldo a pagar'])
        sector['Total saldo a favor'] += int(actividad['Total saldo a favor'])
        
    
    codigo_sector_mayor_ingresos = None
    nombre_sector_mayor_ingresos = None
    ingresos_mayores = 0
    subsecEconomicoMayor = None
    subsecEconomicoMenor = None
    
    #recorrer sectores para saber el mayor
    for codigo, sector in sectores.items():
        if sector['Total ingresos netos'] > ingresos_mayores:
            codigo_sector_mayor_ingresos = codigo
            nombre_sector_mayor_ingresos = sector['Nombre sector económico']
            ingresos_mayores = sector['Total ingresos netos']

    ########### TERMINA LOGICA de SECTORES MAYOR############  


    ########## INCIA LOGICA de SUBSECTORES MAYOR############  
    for actividad in datos['elements']:
        #obtener sector por la actividad economica
        codigo_sec = int(actividad['Código sector económico'])
        codigo_subsector = int(actividad['Código subsector económico'])
        if codigo_sec == codigo_sector_mayor_ingresos:
                if codigo_subsector not in subsectores:
                    subsectores[codigo_subsector] = {
                        'Nombre subsector económico': actividad['Nombre subsector económico'],
                        'Total ingresos netos': 0,
                        'Total de costos y gastos': 0,
                        'Total saldo por pagar': 0,
                        'Total saldo a favor': 0,
                    }
                #se llena la informacion del sector si ya exsiste le suma los valores
                subsector = subsectores[codigo_subsector]
                subsector['Total ingresos netos'] += int(actividad['Total ingresos netos'])
                subsector['Total de costos y gastos'] += int(actividad['Total costos y gastos'])
                subsector['Total saldo por pagar'] += int(actividad['Total saldo a pagar'])
                subsector['Total saldo a favor'] += int(actividad['Total saldo a favor'])

      
    codigo_subsector_mayor_ingresos = None
    nombre_subsector_mayor_ingresos = None
    ingresos_mayores_subsector = 0  
          
    #recorrer sectores para saber el mayor
    for codigo_sub, subsectorMayor in subsectores.items():
        #print(subsector)
        if subsectorMayor['Total ingresos netos'] > ingresos_mayores_subsector:
            codigo_subsector_mayor_ingresos = codigo_sub
            nombre_subsector_mayor_ingresos = subsectorMayor['Nombre subsector económico']
            ingresos_mayores_subsector = subsectorMayor['Total ingresos netos']
                        
    subsecEconomicoMayor = {
        'Código subsector económico': codigo_subsector_mayor_ingresos,
        'Nombre subsector económico': nombre_subsector_mayor_ingresos,
        'Total ingresos netos': ingresos_mayores_subsector,
        'Total de costos y gastos': subsector['Total de costos y gastos'],
        'Total saldo por pagar': subsector['Total saldo por pagar'],
        'Total saldo a favor': subsector['Total saldo a favor'],

    }

    ########## TERMINA LOGICA de SUBSECTORES MAYOR############ 

    ######### INCIA LOGICA de SUBSECTORES MENOR############  
    codigo_subsector_menor_ingresos = None
    nombre_subsector_menor_ingresos = None
    ingresos_menores_subsector = 0            

    if(len(subsectores) > 1) :    
    #recorrer sectores para saber el mayor
        for codigo_sub_men, subsectormen in subsectores.items():
            #print(subsectormen)
            if subsectormen['Total ingresos netos'] < ingresos_menores_subsector:
                codigo_subsector_menor_ingresos = codigo_sub_men
                nombre_subsector_menor_ingresos = subsectormen['Nombre subsector económico']
                ingresos_menores_subsector = subsectormen['Total ingresos netos']
            elif ingresos_menores_subsector == 0:
                ingresos_menores_subsector = int(subsectormen['Total ingresos netos'])
        subsecEconomicoMenor = {
        'Código subsector económico': codigo_subsector_menor_ingresos,
        'Nombre subsector económico': nombre_subsector_menor_ingresos,
        'Total ingresos netos': ingresos_menores_subsector,
        'Total de costos y gastos': subsectormen['Total de costos y gastos'],
        'Total saldo por pagar': subsectormen['Total saldo por pagar'],
        'Total saldo a favor': subsectormen['Total saldo a favor'],
        'Actividad Económica Mayor' : None,
        'Actividad Económica Menor' : None

        }
    else:
        subsecEconomicoMenor = {
        'Código subsector económico': None,
        'Nombre subsector económico': None,
        'Total ingresos netos': None,
        'Total de costos y gastos': None,
        'Total saldo por pagar': None,
        'Total saldo a favor': None,
        'Actividad Económica Mayor' : None,
        'Actividad Económica Menor' : None

        }
    
    ########## TERMINA LOGICA de SUBSECTORES MENOR############ 

    ######### INCIA LOGICA de ACTIVIDADES MAYOR ############  
    for actividad in datos['elements']:
         #obtener sector por la actividad economica
        codigo_sec = int(actividad['Código sector económico'])
        codigo_subsector = int(actividad['Código subsector económico'])
        codigo_act = actividad['Código actividad económica']
        if codigo_sec == codigo_sector_mayor_ingresos:
            if codigo_subsector == codigo_subsector_mayor_ingresos:        
                if codigo_act not in actividades:
                    actividades[codigo_act] = {
                        'Nombre actividad económica': actividad['Nombre actividad económica'],
                        'Total ingresos netos': 0,
                        'Total de costos y gastos': 0,
                        'Total saldo por pagar': 0,
                        'Total saldo a favor': 0,
                    }
                #se llena la informacion del actividad si ya exsiste le suma los valores
                act_subsector = actividades[codigo_act]
                act_subsector['Total ingresos netos'] += int(actividad['Total ingresos netos'])
                act_subsector['Total de costos y gastos'] += int(actividad['Total costos y gastos'])
                act_subsector['Total saldo por pagar'] += int(actividad['Total saldo a pagar'])
                act_subsector['Total saldo a favor'] += int(actividad['Total saldo a favor'])
            elif codigo_subsector == codigo_subsector_menor_ingresos: 
                #llenar lista de actividades menor  
                if codigo_act not in actividadesMenor:
                    actividadesMenor[codigo_act] = {
                        'Nombre actividad económica': actividad['Nombre actividad económica'],
                        'Total ingresos netos': 0,
                        'Total de costos y gastos': 0,
                        'Total saldo por pagar': 0,
                        'Total saldo a favor': 0,
                    }
                #se llena la informacion del actividad si ya exsiste le suma los valores
                act_subsector_menor = actividadesMenor[codigo_act]
                act_subsector_menor['Total ingresos netos'] += int(actividad['Total ingresos netos'])
                act_subsector_menor['Total de costos y gastos'] += int(actividad['Total costos y gastos'])
                act_subsector_menor['Total saldo por pagar'] += int(actividad['Total saldo a pagar'])
                act_subsector_menor['Total saldo a favor'] += int(actividad['Total saldo a favor']) 
      
    codigo_actividad_mayor_ingresos = None
    nombre_actividad_mayor_ingresos = None
    ingresos_mayores_actividad = 0  
           
    #recorrer sectores para saber el mayor
    for codigo_acti, actividadMayor in actividades.items():
        #print(subsector)
        if actividadMayor['Total ingresos netos'] > ingresos_mayores_actividad:
            codigo_actividad_mayor_ingresos = codigo_acti
            nombre_actividad_mayor_ingresos = actividadMayor['Nombre actividad económica']
            ingresos_mayores_actividad = actividadMayor['Total ingresos netos']
                        
    actMayor = {
        'Código Actividad económica': codigo_actividad_mayor_ingresos,
        'Nombre Actividad económica': nombre_actividad_mayor_ingresos,
        'Total ingresos netos': ingresos_mayores_actividad,
        'Total de costos y gastos': act_subsector['Total de costos y gastos'],
        'Total saldo por pagar': act_subsector['Total saldo por pagar'],
        'Total saldo a favor': act_subsector['Total saldo a favor'],

    }

    ########## TERMINA LOGICA de ACTIVIDADES MAYOR############ 

    ########### INCIA LOGICA de ACTIVIDADES MENOR############  
    codigo_actividad_menor_ingresos = None
    nombre_actividad_menor_ingresos = None
    ingresos_menor_actividad = 0  

    if(len(actividades) > 1) :        
        #recorrer sectores para saber el mayor
        for codigo_acti, actividadMenor in actividades.items():
            #print(subsector)
            if actividadMenor['Total ingresos netos'] < ingresos_mayores_actividad:
                codigo_actividad_menor_ingresos = codigo_acti
                nombre_actividad_menor_ingresos = actividadMenor['Nombre actividad económica']
                ingresos_menor_actividad = actividadMenor['Total ingresos netos']
            elif ingresos_menor_actividad == 0:
                ingresos_menor_actividad = int(actividadMenor['Total ingresos netos'])               
        actMenor = {
            'Código Actividad económica': codigo_actividad_menor_ingresos,
            'Nombre Actividad económica': nombre_actividad_menor_ingresos,
            'Total ingresos netos': ingresos_menor_actividad,
            'Total de costos y gastos': act_subsector['Total de costos y gastos'],
            'Total saldo por pagar': act_subsector['Total saldo por pagar'],
            'Total saldo a favor': act_subsector['Total saldo a favor'],

        }

    else:
        actMenor = {
        'Código Actividad económica': None,
        'Nombre Actividad económica': None,
        'Total ingresos netos': None,
        'Total de costos y gastos': None,
        'Total saldo por pagar': None,
        'Total saldo a favor': None,    

        }

    subsecEconomicoMayor['Actividad Económica Mayor'] =  actMayor
    subsecEconomicoMayor['Actividad Económica Menor'] =  actMenor


    ########### INCIA LOGICA de ACTIVIDADES MAYOR DEL MENOR SUBSECTOR############  
    codigo_actividad_mayor_menor_ingresos = None
    nombre_actividad_mayor__menor_ingresos = None
    ingresos_mayor_menor_actividad = 0  

    if(len(actividadesMenor) > 1) :        
        #recorrer sectores para saber el mayor
        for codigo_acti, actividadMayorMenor in actividadesMenor.items():
            #print(subsector)
            if actividadMayorMenor['Total ingresos netos'] > ingresos_mayor_menor_actividad:
                codigo_actividad_mayor_menor_ingresos = codigo_acti
                nombre_actividad_mayor__menor_ingresos = actividadMayorMenor['Nombre actividad económica']
                ingresos_mayor_menor_actividad = actividadMayorMenor['Total ingresos netos']
            elif ingresos_mayor_menor_actividad == 0:
                ingresos_mayor_menor_actividad = int(actividadMayorMenor['Total ingresos netos'])               
        actMayorMenor = {
            'Código Actividad económica': codigo_actividad_mayor_menor_ingresos,
            'Nombre Actividad económica': nombre_actividad_mayor__menor_ingresos,
            'Total ingresos netos': ingresos_mayor_menor_actividad,
            'Total de costos y gastos': actividadMayorMenor['Total de costos y gastos'],
            'Total saldo por pagar': actividadMayorMenor['Total saldo por pagar'],
            'Total saldo a favor': actividadMayorMenor['Total saldo a favor'],

        }

    else:
        actMayorMenor = {
        'Código Actividad económica': None,
        'Nombre Actividad económica': None,
        'Total ingresos netos': None,
        'Total de costos y gastos': None,
        'Total saldo por pagar': None,
        'Total saldo a favor': None,    

        }

    ########### INCIA LOGICA de ACTIVIDADES MENOR DEL MENOR SUBSECTOR############  
    codigo_actividad_menor_menor_ingresos = None
    nombre_actividad_menor__menor_ingresos = None
    ingresos_menor_menor_actividad = 0  

    if(len(actividadesMenor) > 1) :        
        #recorrer sectores para saber el mayor
        for codigo_acti, actividadMenorMenor in actividadesMenor.items():
            #print(subsector)
            if actividadMenorMenor['Total ingresos netos'] < ingresos_menor_menor_actividad:
                codigo_actividad_menor_menor_ingresos = codigo_acti
                nombre_actividad_menor__menor_ingresos = actividadMenorMenor['Nombre actividad económica']
                ingresos_menor_menor_actividad = actividadMenorMenor['Total ingresos netos']
            elif ingresos_menor_menor_actividad == 0:
                ingresos_menor_menor_actividad = int(actividadMenorMenor['Total ingresos netos'])               
        actMenorMenor = {
            'Código Actividad económica': codigo_actividad_menor_menor_ingresos,
            'Nombre Actividad económica': nombre_actividad_menor__menor_ingresos,
            'Total ingresos netos': ingresos_menor_menor_actividad,
            'Total de costos y gastos': actividadMenorMenor['Total de costos y gastos'],
            'Total saldo por pagar': actividadMenorMenor['Total saldo por pagar'],
            'Total saldo a favor': actividadMenorMenor['Total saldo a favor'],

        }

    else:
        actMenorMenor = {
        'Código Actividad económica': None,
        'Nombre Actividad económica': None,
        'Total ingresos netos': None,
        'Total de costos y gastos': None,
        'Total saldo por pagar': None,
        'Total saldo a favor': None,    

        }

    subsecEconomicoMenor['Actividad Económica Mayor'] =  actMayorMenor
    subsecEconomicoMenor['Actividad Económica Menor'] =  actMenorMenor

    secEconomico = {
        'Código sector económico': codigo_sector_mayor_ingresos,
        'Nombre sector económico': nombre_sector_mayor_ingresos,
        'Total ingresos netos': ingresos_mayores,
        'Total de costos y gastos': sector['Total de costos y gastos'],
        'Total saldo por pagar': sector['Total saldo por pagar'],
        'Total saldo a favor': sector['Total saldo a favor'],
        'Subsector Economico Mayor': subsecEconomicoMayor,
        'Subsector Economico Menor': subsecEconomicoMenor,
    }
    
    #buscar el subsector mayor
    #print('secEconomico',secEconomico)

    return secEconomico

def compareRetenciones(data1,data2):
    return int(data1["Total retenciones"]) < int(data2["Total retenciones"])