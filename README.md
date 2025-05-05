# Web Scraping e Análise de Dados de Ações com Python

![GitHub repo size](https://img.shields.io/github/repo-size/LucasRossatto/acoes.py?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/LucasRossatto/acoes.py?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/LucasRossatto/acoes.py?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/LucasRossatto/acoes.py?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/LucasRossatto/acoes.py?style=for-the-badge)


> Este projeto é um script Python que realiza web scraping no site [Investidor10](https://investidor10.com.br/) para extrair dados de ações, como código, nome e valor de mercado. Os dados são salvos em um arquivo CSV e visualizados em um gráfico de barras usando `matplotlib`. Ideal para quem quer aprender sobre automação, análise de dados e visualização com Python.

### Ajustes e Melhorias

O projeto ainda está em desenvolvimento, e as próximas atualizações serão voltadas para as seguintes tarefas:

- [x] Extrair dados de ações do site Investidor10.
- [x] Salvar os dados em um arquivo CSV.
- [x] Gerar um gráfico de barras com `matplotlib`.
- [ ] Adicionar suporte para exportar dados em formato JSON.
- [ ] Implementar agendamento automático para coleta periódica de dados.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente do Python (`>= 3.6`).
- Você instalou as bibliotecas necessárias: `requests`, `beautifulsoup4`, `pandas`, `matplotlib` e `csv`.
- Você tem uma máquina com `Windows`, `Linux` ou `Mac`.
- Você leu a [documentação do BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) e do [Pandas](https://pandas.pydata.org/docs/).

## 🚀 Instalando o Projeto

Para instalar e configurar o projeto, siga estas etapas:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Navegue até a pasta do projeto:

   ```bash
   cd nome-do-repositorio
   pip install requests beautifulsoup4 pandas matplotlib

## ☕ Usando o Projeto
Para executar o script e coletar os dados de ações, siga estas etapas:

1. Execute o script Python:

   ```bash
   python main.py

2.Após a execução, você verá:

Um arquivo acoes.csv com os dados das ações.

Um gráfico de barras mostrando o valor de mercado das ações.


Exemplo de Saída:
CSV (acoes.csv):

Copy
Código,Nome,Valor de Mercado
PETR4,Petróleo Brasileiro S.A.,200.5
VALE3,Vale S.A.,150.3
...

## 📫 Contribuindo para o Projeto
Para contribuir com o projeto, siga estas etapas:

Bifurque este repositório.

Crie um branch: git checkout -b feature/nova-feature.

Faça suas alterações e confirme-as: git commit -m 'Adicionando nova feature'.

Envie para o branch original: git push origin feature/nova-feature.

Crie a solicitação de pull.


Consulte a documentação do GitHub para mais detalhes.

## 🤝 Desenvolvedor

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LucasRossatto" title="Lucas Rossatto">
        <img src="https://avatars.githubusercontent.com/u/154370022?v=4" width="100px;" alt="Foto do Colaborador"/><br>
        <sub>
          <b>Lucas rossatto</b>
        </sub>
      </a>
    </td>
  </tr>
</table>







   
