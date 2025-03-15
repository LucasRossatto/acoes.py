import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import matplotlib.pyplot as plt

url = "https://investidor10.com.br/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

res = requests.get(url, headers=headers)

if res.status_code == 200:
    print("Requisição feita com sucesso")

    soup = BeautifulSoup(res.text, "html.parser")

    ativos = soup.find_all("div", class_="ranking")

    if ativos:
        print("Ações encontradas:")

        dados = []

        with open("acoes.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)

            escritor_csv.writerow(["Código", "Nome", "Valor de Mercado"])

            for index, ativo in enumerate(ativos):
                codigo = ativo.find("h4").text.strip() if ativo.find("h4") else "N/A"
                nome = ativo.find("span").text.strip() if ativo.find("span") else "N/A"
                valor_mercado = (
                    ativo.find("div", class_="ranking-percentage").text.strip()
                    if ativo.find("div", class_="ranking-percentage")
                    else "N/A"
                )

                codigo = re.sub(r"\s+", " ", codigo)
                nome = re.sub(r"\s+", " ", nome)
                valor_mercado = re.sub(r"\s+", " ", valor_mercado)

                escritor_csv.writerow([codigo, nome, valor_mercado])
                dados.append([codigo, nome, valor_mercado])

                print(
                    f"{index + 1}. Código: {codigo}, Nome: {nome}, Valor de Mercado: {valor_mercado}"
                )

        df = pd.DataFrame(dados, columns=["Código", "Nome", "Valor de Mercado"])

        def converter_valor(valor):
            valor = (
                valor.replace("R$", "")
                .replace("US$", "")
                .replace("B", "")
                .replace("M", "")
                .replace("T", "")
            )
            valor = valor.replace(",", ".").strip()
            try:
                return float(valor)
            except ValueError:
                return None

        df["Valor de Mercado"] = df["Valor de Mercado"].apply(converter_valor)

        df = df.dropna(subset=["Valor de Mercado"])

        df.plot(kind="bar", x="Nome", y="Valor de Mercado", color="blue")
        plt.title("Valor de Mercado das Ações")
        plt.xlabel("Nome")
        plt.ylabel("Valor de Mercado")
        plt.show()

        print("Dados salvos em 'acoes.csv'")
    else:
        print("Nenhum ativo encontrado na página.")
else:
    print(f"Erro na requisição: {res.status_code}")
    print(f"Resposta do servidor: {res.text}")
