import time
import matplotlib.pyplot as plt
import numpy as np

#Por não termos um real conexão com o arduino, simulamos  valores para ter uma demonstração mais real
#na medida do possível
talhoes = {
    "Talhao_01": {"umidade": [45, 52, 38, 60, 55], "temp": [28, 30, 32, 29, 31]},
    "Talhao_02": {"umidade": [65, 70, 55, 68, 72], "temp": [25, 26, 27, 24, 25]}
}

#Função que mostra a descrição do nosso projeto
def descricao_projeto():
    print("\n" + "=" * 40)
    print(" | SpaceFarm - Monitoramento via Satélites |")
    print("Integra dados orbitais com sensores locais para agricultura de precisão.")
    print("Objetivo: Reduzir perdas e otimizar recursos hídricos.")

#Função que simula resultados de umidade e temperatura, usando: int(time.time()), para aleatorizar
#valores, usando os segundos em tempo real fazendo o modulo da divisao por 40 e somando 30,
#para sempre retornar um valor entre 30% e 69%, sem precisar utilizar a biblioteca random
def monitoramento_tempo_real():
    print("\n--- Monitoramento em Tempo Real ---")
    for i in range(3):
        umidade = 30 + (int(time.time()) % 40)
        temp = 20 + (int(time.time()) % 15)
        print(f"Umidade do Solo: {umidade}% | Temperatura: {temp}°C")
        if umidade < 45:
            print("⚠️  ALERTA: Umidade crítica! Recomenda irrigação.")
        time.sleep(1)

#Função que puxa os dados de um talhão específico de dentro do dicionário, e exibe ao usuário,
#junto com a média de umidade geral
def historico_talhao():
    talhao = input("Digite o nome do talhão (Talhao_01 ou Talhao_02): ")
    if talhao in talhoes:
        dados = talhoes[talhao]
        print(f"\nHistórico - {talhao}")
        print("Umidade:", dados["umidade"])
        print("Temperatura:", dados["temp"])
        media_u = sum(dados["umidade"]) / len(dados["umidade"])
        print(f"Média de Umidade: {media_u:.1f}%")
    else:
        print("Talhão não encontrado.")

#Diferentiated Problem Solving- Função que gera um gráfico
def gerar_relatorio():
    print("\n=== Relatório da Fazenda ===")
    for talhao, dados in talhoes.items():
        media_u = sum(dados["umidade"]) / len(dados["umidade"])
        print(f"{talhao} - Média Umidade: {media_u:.1f}%")

    # Gráfico simples
    plt.figure(figsize=(8, 5))
    plt.plot(talhoes["Talhao_01"]["umidade"], label="Talhao_01", marker='o')
    plt.plot(talhoes["Talhao_02"]["umidade"], label="Talhao_02", marker='o')
    plt.title("Evolução da Umidade do Solo")
    plt.xlabel("Leituras")
    plt.ylabel("Umidade (%)")
    plt.legend()
    plt.grid(True)
    plt.show()

#Função que exibe o menu
def menu():
    while True:
        print("\n" + "=" * 40)
        print("              MENU - AGROSAT")
        print("=" * 40)
        print("1. Descrição do Projeto")
        print("2. Monitoramento em Tempo Real")
        print("3. Histórico por Talhão")
        print("4. Gerar Relatório Completo")
        print("5. Simular Alerta de Seca")
        print("0. Sair")
        print("=" * 40)

        op = input("Escolha uma opção: ")

        if op == "1":
            descricao_projeto()
        elif op == "2":
            monitoramento_tempo_real()
        elif op == "3":
            historico_talhao()
        elif op == "4":
            gerar_relatorio()
        elif op == "5":
            print("\nSimulando condição de seca...")
            for i in range(5, 0, -1):
                print(f"Umidade caindo... {i * 10}%")
                time.sleep(0.6)
            print("🚨 ALERTA CRÍTICO: Risco alto de perda da lavoura!")
        elif op == "0":
            print("Saindo do sistema. Obrigado por usar SpaceFarm! 🌍🚀")
            break
        else:
            print("Opção inválida!")

menu()
