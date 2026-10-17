# Data Summary Report - Empregabilidade Jovem no Brasil

## Visão Geral

O projeto utiliza diferentes fontes de dados para analisar aspectos relacionados à empregabilidade jovem no Brasil.

Os dados são armazenados em arquivos estruturados e textos processados dentro da pasta `data/`.

## Indicadores de Empregabilidade

### Fonte

IBGE / SIDRA.

### Arquivo

`data/sample/empregabilidade_jovem.csv`

### Principais Campos

- `uf`
- `estado`
- `regiao`
- `taxa_desocupacao`

### Utilização

Os dados são utilizados para:

- Filtrar indicadores por região.
- Filtrar indicadores por estado.
- Comparar estados.
- Gerar gráficos.
- Disponibilizar consultas por meio da API FastAPI.

## Notícias sobre Empregabilidade

### Fonte

Agência Brasil.

### Método de Coleta

Requests e BeautifulSoup.

### Arquivo Processado

`data/processed/noticias_empregabilidade.csv`

### Principais Campos

- `titulo`
- `data`
- `url`
- `fonte`

### Utilização

As notícias são apresentadas na aplicação e utilizadas para análise de frequência de palavras presentes nos títulos.

## Dados Enviados pelo Usuário

A aplicação permite o envio de arquivos CSV contendo notícias adicionais.

Os arquivos passam por validação antes de serem utilizados.

Os registros enviados pelo usuário são identificados separadamente dos registros coletados pela Web para preservar a procedência dos dados.

## Dados Recebidos pela API

A API FastAPI possui uma rota POST que permite o envio de novas notícias.

Os registros são armazenados em:

`data/processed/noticias_api.csv`

A aplicação também permite consultar esses registros por meio de uma rota GET.

## Coleta Dinâmica com Selenium

### Fonte

Painel das Juventudes da Bahia.

### Método

Selenium com navegador Chrome automatizado.

### Arquivo

`data/processed/painel_juventudes_trabalho.txt`

### Processo

O Selenium acessa a página utilizando um navegador automatizado, aguarda o carregamento do documento, executa a navegação necessária e coleta o conteúdo textual disponível.

A coleta é executada separadamente da aplicação Streamlit.

### Utilização

O conteúdo coletado é apresentado na página "Dados Dinâmicos" da aplicação.

Essa fonte é utilizada como informação complementar sobre juventudes e não substitui os indicadores nacionais do IBGE.

## API FastAPI

A API não representa uma nova fonte de dados.

Ela funciona como uma nova forma de acesso aos dados existentes no projeto.

As principais rotas permitem:

- Consulta de indicadores.
- Consulta de indicadores por UF.
- Filtro por região.
- Consulta de notícias recebidas.
- Envio de novas notícias.

## Qualidade e Limitações

Os dados do IBGE são utilizados como principal referência quantitativa do projeto.

As notícias e os dados coletados pela Web possuem finalidade complementar.

O Painel das Juventudes da Bahia possui recorte estadual e, portanto, não deve ser interpretado como representação de todo o Brasil.

A disponibilidade das informações obtidas por Web Scraping ou Selenium pode depender de alterações realizadas nos sites de origem.

## Preparação dos Dados para LLMs

O projeto possui dois tipos principais de informação que poderão ser utilizados por modelos de linguagem:

- Dados estruturados de indicadores.
- Dados textuais provenientes de notícias e coleta Web.

Em etapas futuras, esses dados poderão ser utilizados para:

- Resumir notícias.
- Gerar explicações dos indicadores.
- Criar relatórios automáticos.
- Responder perguntas sobre empregabilidade jovem.
- Comparar regiões utilizando linguagem natural.

A combinação de dados estruturados e conteúdo textual permite preparar o projeto para uma futura arquitetura de geração aumentada por dados do próprio projeto.