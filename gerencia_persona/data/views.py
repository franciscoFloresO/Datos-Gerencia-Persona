from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.contrib import messages
import pandas as pd
from .models import HorasExtras, Disponibilidad, HorasCompensadas, Pais, Provision

def menu_data(request):
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    years_actual = datetime.now().year
    years = range(years_actual - 1, years_actual + 2) 
    paises = Pais.objects.all()
    return render(request,'menu_data.html',{
        'meses':meses, 
        'years':years,
        'paises':paises})


def visualizar_horas_extras(request):
    horas_extras = HorasExtras.objects.all()
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    years_actual = datetime.now().year
    years = range(years_actual - 1, years_actual + 2) 
    return render(request,'visualizar_horas_extras.html',{
        'horas_extras':horas_extras,
        'meses':meses,
        'years':years
    })

def visualizar_provisiones(request):
    provisiones = Provision.objects.all()
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    years_actual = datetime.now().year
    years = range(years_actual - 1, years_actual + 2) 
    return render(request,'visualizar_provisiones.html',{
        'provisiones':provisiones,
        'meses':meses,
        'years':years
    })

def visualizar_horas_compensadas(request):
    horas_compensadas = HorasCompensadas.objects.all()
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    years_actual = datetime.now().year
    years = range(years_actual - 1, years_actual + 2) 
    return render(request,'visualizar_horas_compensadas.html',{
        'horas_compensadas':horas_compensadas,
        'meses':meses,
        'years':years
    })

def visualizar_disponibilidad(request):
    disponibilidades = Disponibilidad.objects.all()
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    years_actual = datetime.now().year
    years = range(years_actual - 1, years_actual + 2) 
    return render(request,'visualizar_disponibilidad.html',{
        'disponibilidades':disponibilidades,
        'meses':meses,
        'years':years
    })

def visualizar(request):
    return render(request,'visualizar.html')



def cargar_horas_extras(request):
    if request.method == 'POST' and request.FILES.get('excelFile'):
        pais = request.POST.get('pais_horas_extras')
        year = request.POST.get('year_horas_extras')
        mes = request.POST.get('mes_horas_extras')         
        archivo_excel = request.FILES['excelFile']
        datos_por_hoja = pd.read_excel(archivo_excel, sheet_name=None)
        mensajes = []  # Lista para almacenar los mensajes

        # Diccionario para mapear los nombres de las hojas a los modelos correspondientes
        modelos = {
            "Horas extras": HorasExtras,
            "Disponibilidad": Disponibilidad,
            "Horas compensadas": HorasCompensadas,

        }

        for nombre_hoja, datos_excel in datos_por_hoja.items():
            datos_excel_filtrados = datos_excel.loc[(datos_excel['País'].str.lower()==pais.lower()) & (datos_excel['Año']==int(year)) & (datos_excel['Mes']==int(mes))]

            try:
                modelo = modelos.get(nombre_hoja)
                if modelo:
                    procesar_datos(modelo, datos_excel_filtrados, pais, year, mes, nombre_hoja)
                    mensajes.append({'tipo': 'success', 'mensaje': f'Carga de información de "{nombre_hoja}" correcta.'})
                else:
                    raise ValueError(f"No se encontró un modelo asociado para la hoja '{nombre_hoja}'.")
            except Exception as e:
                mensajes.append({'tipo': 'error', 'mensaje': str(e)})
                return JsonResponse({'mensajes': mensajes})

        return JsonResponse({'mensajes': mensajes})

    return JsonResponse({'mensajes': []}) 


def procesar_datos(modelo, datos_excel_filtrados, pais, year, mes, nombre_hoja):

    filtered_data = datos_excel_filtrados.dropna(subset=['País','Empresa', 'ID Sonda Plus', 'Año', 'Mes', 'Numero de documento', 'Nombre del colaborador', 'Monto', 'Cantidad de Horas', 'Moneda', 'Centro de costos(Código)'], how='all')
    existing_data = modelo.objects.filter(year=year, mes=mes, pais=pais)
    if existing_data.exists():
        print("Se encontró información existente en la base de datos. Eliminando...")
        existing_data.delete() 

    for index, row in filtered_data.iterrows():

        row.fillna(0, inplace=True)
        
        
        try:
            year = int(row['Año'])
            mes = int(row['Mes'])
            id_sonda_plus = int(row['ID Sonda Plus'])
            monto = float(row['Monto'])
            cantidad_horas = float(row['Cantidad de Horas'])
            centro_costo = int(row['Centro de costos(Código)'])
        except ValueError:
            raise ValueError(f"Data no válida en hoja'{nombre_hoja}', fila {index + 2}: revisar formato del dato. ")
        
        
        try:
            info = modelo(
                pais=row['País'],
                id_sonda_plus=id_sonda_plus,
                year=year,
                mes=mes,
                numero_documento=row['Numero de documento'],
                nombre_colaborador=row['Nombre del colaborador'],
                monto=monto,
                cantidad_horas=cantidad_horas,
                moneda=row['Moneda'],
                centro_costos=centro_costo,
                empresa=row['Empresa']
            )
            print("Objeto info creado:", info)
            info.save()
            print("Datos guardados exitosamente")
        except Exception as e:
            print("Error al crear o guardar el objeto:", e)
    
    print("Proceso de carga de datos completado.")
    return True


def cargar_provisiones(request):
    if request.method == 'POST' and request.FILES.get('excelFile_p'):
        print('POST')
        pais = request.POST.get('pais_provisiones')
        year = request.POST.get('year_provisiones')
        mes = request.POST.get('mes_provisiones')         
        archivo_excel = request.FILES['excelFile_p']
        print(archivo_excel)
        datos_por_hoja = pd.read_excel(archivo_excel, sheet_name=None)
        mensajes = []  # Lista para almacenar los mensajes

        for nombre_hoja, datos_excel in datos_por_hoja.items():
            nombre_de_la_hoja_actual = nombre_hoja
            datos_filtrados = datos_excel.loc[(datos_excel['País'].str.lower()==pais.lower()) & (datos_excel['Año']==int(year)) & (datos_excel['Mes']==int(mes))]
            
            try:
                procesar_datos_provision(datos_filtrados, pais, year, mes, nombre_de_la_hoja_actual)
                mensajes.append({'tipo': 'success', 'mensaje': 'Carga de información correcta.'})
            except ValueError as e:
                mensajes.append({'tipo': 'error', 'mensaje': str(e)})
                print(f'EL ERROR DE CARGAR EXCEL ', str(e))
                request.session['mensaje'] = str(e)
                return JsonResponse({'mensajes': mensajes})
        
        return JsonResponse({'mensajes': mensajes})

    return JsonResponse({'mensajes': []}) 

def procesar_datos_provision(datos_filtrados, pais, year, mes, nombre_de_la_hoja_actual):
    filtered_data = datos_filtrados.dropna(subset=['País', 'Año', 'Mes', 'Empresa', 'Id SONDA PLUS', 'Numero Documento', 'Primer Nombre', 'Primer Apellido', 'Segundo Apellido', 'Cod Centro de Costo', 'Saldo Cantidad días  (#)', 'Saldo Monto','Moneda'], how='all')
    existing_data = Provision.objects.filter(year=year, pais=pais, mes=mes)

    if existing_data.exists():
        print(f"Se encontró información existente en la base de datos. Eliminando...", nombre_de_la_hoja_actual)
        existing_data.delete() 

    for index, row in filtered_data.iterrows():
        row.fillna(0, inplace=True)
        try:
            year = int(row['Año'])
            mes = int(row['Mes'])
            id_sonda_plus = int(row['Id SONDA PLUS'])   
            monto = float(row['Saldo Monto'])
            cantidad_dias = float(row['Saldo Cantidad días  (#)'])
            centro_costo = int(row['Cod Centro de Costo'])
        except ValueError:
            raise ValueError(f"Data no válida en fila {index + 2}: revisar formato del dato. ")
        
        info = Provision(
            pais=row['País'],
            id_sonda_plus=id_sonda_plus,
            year=year,
            mes=mes,
            numero_documento=row['Numero Documento'],
            nombre=row['Primer Nombre'],
            primer_apellido=row['Primer Apellido'],
            segundo_apellido=row['Segundo Apellido'],
            saldo_monto=monto,
            cantidad_dias=cantidad_dias,
            moneda=row['Moneda'],
            centro_costos=centro_costo,
            empresa=row['Empresa']
        )
        info.save()
        print(f"Guardando Provisiones ", nombre_de_la_hoja_actual)
    
    print("Proceso de carga de datos completado.")
    return True
