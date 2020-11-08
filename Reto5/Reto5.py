# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 08:18:06 2020

@author: Michael Arias
"""

import pandas as pd
#import matplotlib

def caso_who(ruta_archivo_csv: str)-> dict:
    # Validadciones
    # 1 Extension
    if ruta_archivo_csv.endswith('.csv'): # or (ruta_archivo_csv[-4:] == '.csv')
        # 2 Open File (ruta_archivo_csv)
        try:
            dt = pd.read_csv(ruta_archivo_csv)
        except:
            return 'Error al leer el archivo de datos.'        
        
        # Una vez realizadas las validaciones entonces calculamos
        # Transformar el formato de fechas para establecer como indice
        dt['date'] = pd.to_datetime(dt['date'])
        # Determinar la razon promedio
        total_cases_per_million = pd.Series(dt['total_cases_per_million'])
        population = pd.Series(dt['population'])
        hospital_beds_per_thousand = dt['hospital_beds_per_thousand']
        dt['promedio'] = (( total_cases_per_million * population) / 1000000 ) / (( hospital_beds_per_thousand * population ) / 1000 )
        df_respuesta = dt.groupby(['date', 'continent' ])['promedio'].mean()
        df_respuesta = df_respuesta.unstack()
        # or df_respuesta = dt.pivot_table(index='date', columns='continent', values='promedio', aggfunc='mean')
        df_respuesta.plot()
        # df_respuesta.index df_respuesta.columns
                
    else:
        return 'Extensión inválida.'    
        
    # Preparar Salida
    df_respuesta = df_respuesta.to_dict()
    return df_respuesta

print(caso_who('owid-covid-data.csv'))