# Web Scraping de Worksheets - AgendaWeb

Este projeto foi desenvolvido como atividade prática da disciplina de Linguagem de Programação II.

A proposta consiste na criação de um script em Python capaz de realizar web scraping no site AgendaWeb, com o objetivo de coletar automaticamente links de worksheets (folhas de exercícios) disponíveis na página.

A motivação do projeto surgiu a partir de uma necessidade real. Como professora de inglês, eu frequentemente busco por materiais complementares e exercícios. Este projeto automatiza esse processo, permitindo a extração rápida e organizada dos links disponíveis.


## Funcionalidades

- Acessa automaticamente a página de exercícios de gramática do AgendaWeb
- Realiza o parsing do conteúdo HTML da página
- Extrai links válidos de worksheets
- Exibe os resultados no terminal
- Salva os links em um arquivo `worksheets.txt`


## Como funciona

O script executa as seguintes etapas:

1. Envia uma requisição HTTP para a página alvo
2. Analisa o HTML utilizando BeautifulSoup
3. Identifica e filtra os elementos de link (`<a href="...">`)
4. Armazena os links encontrados
5. Exibe os resultados no terminal
6. Salva os dados em um arquivo de texto


## Tecnologias utilizadas

- Python 3
- requests
- BeautifulSoup


## Como executar o projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

Clone o repositório:

```bash
git clone https://github.com/nataliathomazelliferreira/Web-Scraping.git
````

Acesse o diretório do projeto:

```bash
cd Web-Scraping
```

Crie um ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o script:

```bash
python procurando_worksheets.py
```

## Exemplo de saída

Links salvos em worksheets.txt

## Dependências

```
beautifulsoup4==4.14.3
certifi==2026.2.25
charset-normalizer==3.4.7
idna==3.11
requests==2.33.1
soupsieve==2.8.3
typing_extensions==4.15.0
urllib3==2.6.3
```

## Melhorias futuras

* Filtrar worksheets por categoria ou nível
* Implementar um menu simples, para escolher qual conteúdo deseja



