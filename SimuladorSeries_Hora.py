import random
from datetime import datetime, timedelta

# Configurações
data_inicial = datetime(2023, 7, 1)
data_final = datetime(2023, 7, 31)
hora_inicial = 0
hora_final = 23

# Função para gerar dados de vazão afluente
def gerar_vazao():
    return round(random.uniform(900, 1300), 2)

# Simulação
dados_simulados = []

data_atual = data_inicial
while data_atual <= data_final:
    hora_atual = hora_inicial
    while hora_atual <= hora_final:
        timestamp = data_atual + timedelta(hours=hora_atual)
        vazao = gerar_vazao()
        dados_simulados.append({"timestamp": timestamp, "vazao": vazao})
        hora_atual += 1
    data_atual += timedelta(days=1)

# Exibição dos dados simulados (opcional)
for dado in dados_simulados:
    print(f"{dado['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}: {dado['vazao']:.2f}")

# Salvar os dados simulados em um arquivo CSV (opcional)
import csv

with open("dados_simulados.csv", "w", newline="") as csvfile:
    fieldnames = ["timestamp", "vazao"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for dado in dados_simulados:
        writer.writerow({"timestamp": dado["timestamp"].strftime("%Y-%m-%d %H:%M:%S"), "vazao": f"{dado['vazao']:.2f}"})
