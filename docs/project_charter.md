# Project Charter - Empregabilidade Jovem no Brasil

## Problema de Negócio

A inserção de jovens no mercado de trabalho brasileiro apresenta diferenças entre estados e regiões. O projeto busca organizar e apresentar dados relacionados à empregabilidade jovem de forma acessível, permitindo a comparação de indicadores e o acompanhamento de informações complementares relacionadas às juventudes.

## Objetivo Geral

Desenvolver uma aplicação interativa para consulta e comparação de indicadores relacionados à empregabilidade jovem no Brasil, integrando dados públicos, coleta Web e uma API própria.

## Objetivos Específicos

- Comparar indicadores de empregabilidade jovem entre estados e regiões brasileiras.
- Identificar diferenças nas taxas de desocupação dos jovens.
- Apresentar notícias relacionadas à empregabilidade jovem.
- Organizar a aplicação em múltiplas páginas de acordo com suas funcionalidades.
- Disponibilizar os dados por meio de uma API desenvolvida com FastAPI.
- Integrar a aplicação Streamlit com a API.
- Ampliar a coleta de dados utilizando Web Scraping e Selenium.
- Preparar os dados e a arquitetura do projeto para futuras funcionalidades utilizando LLMs.

## Escopo do TP3

O TP3 amplia o projeto desenvolvido anteriormente com os seguintes recursos:

- Aplicação Streamlit organizada em múltiplas páginas.
- Navegação entre indicadores, comparador, notícias, dados dinâmicos e API.
- API desenvolvida com FastAPI.
- Rotas GET para consulta de indicadores.
- Rota POST para recebimento de novas notícias.
- Integração entre Streamlit e FastAPI.
- Coleta de dados utilizando Selenium.
- Armazenamento dos dados coletados em arquivos na pasta `data/`.
- Preparação para futura integração com modelos de linguagem.

## Fontes de Dados

- IBGE / SIDRA para indicadores de empregabilidade.
- Agência Brasil para notícias relacionadas à empregabilidade jovem.
- Painel das Juventudes da Bahia para dados complementares coletados com Selenium.
- Arquivos CSV enviados pelo usuário.

## Stakeholders

- Jovens interessados em informações sobre mercado de trabalho.
- Pesquisadores e estudantes.
- Gestores e profissionais interessados em indicadores de juventude.
- Usuários da aplicação Streamlit.
- Sistemas e aplicações externas que podem consumir os dados por meio da API.

## Tecnologias Utilizadas

- Python
- Streamlit
- FastAPI
- Requests
- BeautifulSoup
- Selenium
- CSV
- Git e GitHub

## Decisão sobre Selenium

No TP2, a coleta de notícias da Agência Brasil foi realizada com Requests e BeautifulSoup, pois as informações necessárias estavam disponíveis diretamente no HTML.

No TP3, Selenium foi utilizado como complemento para acessar o Painel das Juventudes da Bahia utilizando um navegador automatizado. A coleta é executada separadamente da aplicação e o resultado é armazenado em `data/processed/painel_juventudes_trabalho.txt`.

## Integração com FastAPI

A API permite que os dados do projeto também sejam utilizados por outros programas.

Foram implementadas rotas para:

- Consultar todos os indicadores.
- Filtrar indicadores por região.
- Consultar indicadores por UF.
- Consultar notícias recebidas pela API.
- Enviar novas notícias por meio de uma requisição POST.

A aplicação Streamlit possui uma página específica que consome essas rotas.

## Preparação para Uso de LLMs

O projeto foi estruturado para permitir a introdução de modelos de linguagem em etapas futuras.

Possíveis aplicações incluem:

- Resumo automático das notícias coletadas.
- Classificação e análise de textos relacionados ao mercado de trabalho.
- Geração automática de relatórios a partir dos indicadores.
- Sistema de perguntas e respostas sobre os dados do projeto.
- Geração de explicações em linguagem natural sobre diferenças entre estados e regiões.

Os dados estruturados de indicadores e os textos coletados poderão ser utilizados como contexto para essas funcionalidades.

## Critérios de Sucesso

O projeto será considerado bem-sucedido quando permitir:

- Navegação entre múltiplas páginas.
- Consulta e comparação dos indicadores.
- Visualização das notícias coletadas.
- Consulta de dados coletados dinamicamente.
- Comunicação entre Streamlit e FastAPI.
- Utilização de rotas GET e POST.
- Organização dos dados para utilização futura com LLMs.