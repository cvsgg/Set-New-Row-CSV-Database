#Bibliotecas padrão
import json
import csv

#Nova Série JSON - Ref Ministerio de Minas e Energia Brasil
new_serie = {'REF_AREA': 'BR',
             'TIME_PERIOD': '2020-01-01',
             'ENERGY_PRODUCT': 'Gross Domestic Product',
             'UNIT_MEASURE': 'US/INH',
             'OBS_VALUE': '13.44'}

# Abre banco de dados .csv
with open('dados/jodi_gas_beta.csv', 'a+') as database:
    # Define os campos
    fields = ['REF_AREA', 'TIME_PERIOD', 'ENERGY_PRODUCT', 'FLOW_BREAKDOWN', 'UNIT_MEASURE', 'OBS_VALUE',
              'ASSESSMENT_CODE']
    # Converte a dict para inserção dos dados
    dict = {'REF_AREA': 'BR', 'TIME_PERIOD': '2020-01-01', 'ENERGY_PRODUCT': 'Gross Domestic Product',
            'UNIT_MEASURE': 'US/INH', 'OBS_VALUE': '13.44'}
    # Inclui linha na base de dados
    dictwriter_object = DictWriter(database, fieldnames=fields)
    dictwriter_object.writerow(dict)

database.close()
