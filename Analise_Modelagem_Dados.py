
# Import libraries
import pandas as pd
import numpy as np
from datetime import date, datetime as dt

# Definindo funções

def primeiro_quartil(vetor):
    return vetor.quantile(.25)

def terceiro_quartil(vetor):
    return vetor.quantile(.75)

def alcance_inter_quartil(vetor):
    return terceiro_quartil(vetor) - primeiro_quartil(vetor)

def limite_inferior(vetor):
    return primeiro_quartil(vetor) - 1.5 * alcance_inter_quartil(vetor)

def limite_superior(vetor):
    return terceiro_quartil(vetor) + 1.5 * alcance_inter_quartil(vetor)

# Read data

url_link = 'https://storage.googleapis.com/focus-bi/temperature_load.csv'
data = pd.read_csv(url_link, sep=';', index_col='Date').dropna(how='all')
data.index = [dt.strptime(x, "%d/%m/%Y").date() for x in data.index]
# Get Temperature and Load Data
start_date = date(2020, 1, 1)
end_date = date(2020, 12, 31)
temperature = data.loc[start_date:end_date, 'Temperature']
load = data.loc[start_date:end_date, 'Load']

# Write your code here
print("Analisando Dados")

print("Primeiro Quartil",+ primeiro_quartil(temperature))
print("Terceiro Quartil",+ terceiro_quartil(temperature))

limite_superior_temperatura = limite_superior(temperature)
limite_inferior_temperatura = limite_inferior(temperature)

print("IQR",+ alcance_inter_quartil(temperature))

print("UB",+ limite_superior_temperatura)
print("LB",+ limite_inferior_temperatura)

print("Não existe índice com exato valor do UP e LB")

temperature[temperature > limite_superior_temperatura].index
temperature[temperature > limite_superior_temperatura] = limite_superior_temperatura

media = sum(temperature)
desviopadrao = np.std(temperature)

print()
print("Criado nova série de temperatura")
print("substituido os outliers pelos valores dos limites inferiores LB ou superiores UB.")
print("verificar valor temperature")
print("Média",+media)
print("Desvio Padrão",+desviopadrao)

start_date = date(2020, 12, 25)
end_date = date(2020, 12, 31)
temperature_new = data.loc[start_date:end_date, 'Temperature']
load = data.loc[start_date:end_date, 'Load']
temperature_new.rolling(7).mean()
load.rolling(7).mean()

print()
print("Gerado Série temporal de 7 Dias")
print("Entre 25/12/2020 e 31/12/2021")

X = temperature_new.rolling(7).mean()
Y = load.rolling(7).mean()
X = X.fillna(0)
Y = Y.fillna(0)
fit = np.polyfit(X, Y, 1)
ang_coeff = fit[0]
intercept = fit[1]
x = np.array(np.linspace(1,7,7))
z = np.dot(ang_coeff,x) + intercept

print()
print("d)")
print("A reta fica:")
print("Y =",ang_coeff, "* X + ",+ intercept)

df = pd.DataFrame({'Load': [z[0],z[1],z[2],z[3],z[4],z[5],z[6]]},
                  index = [pd.Timestamp('20210101'),
                           pd.Timestamp('20210102'),
                           pd.Timestamp('20210103'),
                           pd.Timestamp('20210104'),
                           pd.Timestamp('20210105'),
                           pd.Timestamp('20210106'),
                           pd.Timestamp('20210107')])
print()
print("Valores de carga de 01/01/2021 a 07/01/2021 são")
print(df)

