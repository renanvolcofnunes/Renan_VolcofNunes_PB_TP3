# Empregabilidade Jovem no Brasil

Projeto desenvolvido para a disciplina Projeto de Bloco: Inteligência Artificial Aplicada.

O projeto analisa indicadores relacionados à empregabilidade de jovens no Brasil e reúne dados públicos, notícias e informações complementares sobre juventudes.

No TP3, a aplicação foi ampliada com navegação multipáginas, API FastAPI, integração HTTP entre Streamlit e API, coleta Web com BeautifulSoup, coleta dinâmica com Selenium e preparação para futuras funcionalidades utilizando LLMs.

## Funcionalidades do TP3

- Navegação entre múltiplas páginas com Streamlit.
- Filtros de indicadores por região e estado.
- Comparação das taxas de desocupação entre estados.
- Visualização de tabelas e gráficos.
- Coleta de notícias com Requests e BeautifulSoup.
- Upload e validação de arquivos CSV.
- Download dos indicadores filtrados.
- API desenvolvida com FastAPI.
- Rotas GET para consulta de indicadores.
- Rota POST para envio de notícias.
- Integração HTTP entre Streamlit e FastAPI.
- Coleta dinâmica utilizando Selenium.
- Visualização dos dados coletados pelo Selenium.
- Preparação para futura utilização de LLMs.

## Estrutura do Projeto

- `app.py`: aplicação principal.
- `comum.py`: funções compartilhadas.
- `paginas/`: páginas da aplicação Streamlit.
- `api/main.py`: API FastAPI.
- `src/data_access.py`: acesso aos indicadores.
- `src/coleta_web.py`: coleta com Requests e BeautifulSoup.
- `src/coleta_dinamica.py`: coleta com Selenium.
- `data/sample/`: dados utilizados pela aplicação.
- `data/processed/`: dados processados.
- `docs/`: documentação do projeto.

A pasta `data/raw/` é criada durante a coleta Web e armazena os arquivos HTML obtidos. Esses arquivos são ignorados pelo Git e não fazem parte do repositório.

## Ambiente de Desenvolvimento

Criar o ambiente virtual:

```powershell
python -m venv .venv
```

Os comandos abaixo devem ser executados no PowerShell, na raiz do projeto. Use Python 3.10 ou superior.

Ativar o ambiente virtual e instalar as dependências da aplicação e da API:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-api.txt
```

Caso o PowerShell bloqueie a ativação de scripts, libere apenas a sessão atual e tente novamente:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Execução Local

No primeiro terminal, com a `.venv` ativada, iniciar a API:

```powershell
python -m uvicorn api.main:app
```

A API fica disponível em http://127.0.0.1:8000 e a documentação interativa em http://127.0.0.1:8000/docs. O comando é usado sem `--reload`, pois a execução com recarga apresentou `WinError 2` no ambiente Windows utilizado na validação.

Em outro terminal, abrir a mesma pasta do projeto, ativar o ambiente e iniciar o Streamlit:

```powershell
.\.venv\Scripts\Activate.ps1
python -m streamlit run app.py
```

Abrir http://localhost:8501 e manter os dois terminais em execução. Para encerrar cada serviço, usar `Ctrl+C` no respectivo terminal.

### Integração HTTP e validação

A página **API** do Streamlit utiliza `requests.get` e `requests.post` para fazer requisições HTTP reais à API FastAPI em http://127.0.0.1:8000, executada pelo Uvicorn em um processo separado.

Rotas disponíveis:

- `GET /`: mensagem inicial da API.
- `GET /indicadores`: consulta dos indicadores; aceita o filtro opcional `regiao`.
- `GET /indicadores/{uf}`: consulta dos indicadores de uma UF, por exemplo `/indicadores/SP`.
- `GET /noticias`: consulta das notícias recebidas pela API.
- `POST /noticias`: envio de uma notícia com os campos `titulo`, `data`, `url` e `fonte`; retorna status 201 e grava os dados em `data/processed/noticias_api.csv`.

Para validar, acessar a página **API**, selecionar uma UF e consultar os indicadores. Em seguida, preencher o formulário de notícia, enviar e consultar as notícias recebidas. O POST modifica o CSV local; notícias criadas apenas para teste devem ser removidas após a validação, sem descartar dados que precisem ser preservados.

Na validação local realizada, a consulta de SP retornou um registro com taxa de desocupação de 12,2%, e o envio e a consulta de notícias confirmaram a integração HTTP e a persistência no CSV.

A URL base pode ser configurada pela variável de ambiente `EMPREGABILIDADE_API_URL`, definida no terminal do Streamlit antes de iniciá-lo. Sem essa configuração, o endereço utilizado é http://127.0.0.1:8000.

### Streamlit Community Cloud

No Streamlit Community Cloud, `127.0.0.1` aponta para o ambiente do serviço em nuvem, não para o computador do usuário. Como iniciar o Streamlit não inicia automaticamente o Uvicorn, a página API pode exibir **“A API não está disponível”** quando não há uma API acessível nesse endereço.

Essa limitação do ambiente publicado não invalida o teste local: a integração foi validada com Streamlit e FastAPI em execução simultânea no computador. Para utilizar essa página na nuvem, seria necessário disponibilizar uma API acessível pelo serviço e configurar `EMPREGABILIDADE_API_URL`.

## Coleta Web com BeautifulSoup

O script `src/coleta_web.py` utiliza Requests e BeautifulSoup para coletar notícias da Agência Brasil. Ele consulta `robots.txt`, verifica a permissão para cada URL, identifica o agente de coleta e respeita o intervalo informado, com espera padrão de 10 segundos quando não há `crawl-delay`.

Executar a partir da raiz do projeto, com a `.venv` ativada:

```powershell
python src/coleta_web.py
```

Os HTMLs são salvos localmente em `data/raw/`. O script extrai título, data de publicação, URL e fonte para `data/processed/noticias_empregabilidade.csv`. Quando nenhuma notícia é coletada, o CSV anterior é preservado. A coleta depende da disponibilidade e da estrutura das páginas de origem.

`data/raw/` é uma pasta de trabalho local: os arquivos HTML são ignorados pelo Git pela regra `data/raw/*.html` e não são necessários para executar a aplicação com os dados processados já presentes no repositório.

## Coleta Dinâmica com Selenium

O script `src/coleta_dinamica.py` abre o Painel das Juventudes da Bahia com Selenium e Chrome, aguarda o carregamento do documento, rola a página e extrai o texto disponível no corpo da página. O navegador é fechado ao final da tentativa de coleta.

Instalar as dependências adicionais e executar:

```powershell
python -m pip install -r requirements-coleta.txt
python src/coleta_dinamica.py
```

É necessário ter o Google Chrome instalado e um driver compatível disponível para o Selenium; o gerenciamento automático pode precisar de conexão à internet. O resultado é salvo em `data/processed/painel_juventudes_trabalho.txt` e exibido na página **Dados Dinâmicos**. A coleta depende da disponibilidade e do conteúdo carregado pelo site de origem.

## Dados e Arquivos Processados

- `data/sample/empregabilidade_jovem.csv`: indicadores utilizados no dashboard e na API, com UF, estado, região, faixa etária, taxa de desocupação e trimestre.
- `data/processed/noticias_empregabilidade.csv`: notícias obtidas com Requests e BeautifulSoup, com título, data, URL e fonte.
- `data/processed/noticias_api.csv`: notícias recebidas pela rota POST da API, com título, data, URL e fonte.
- `data/processed/painel_juventudes_trabalho.txt`: texto coletado com Selenium no painel de juventudes.
- `data/raw/`: HTMLs locais da coleta Web, ignorados pelo Git conforme a regra descrita acima.

Os indicadores podem ser atualizados com `python src/data_access.py`, que consulta o SIDRA e a API de localidades do IBGE e sobrescreve `data/sample/empregabilidade_jovem.csv`. Essa atualização exige conexão à internet e pode alterar o trimestre e os valores apresentados. Não é necessário refazer as coletas para consultar os arquivos já incluídos no projeto.

## Fontes

- [IBGE — SIDRA, tabela 4094](https://sidra.ibge.gov.br/tabela/4094): indicadores de desocupação; a consulta do projeto utiliza a variável 4099, o grupo etário de 18 a 24 anos e o último trimestre disponível.
- [IBGE — API de localidades](https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome): identificação de estados, UFs e regiões.
- [Agência Brasil](https://agenciabrasil.ebc.com.br/): notícias sobre empregabilidade e juventude; as URLs específicas ficam registradas no script e no CSV processado.
- [Painel das Juventudes da Bahia — SEI](https://infovis.sei.ba.gov.br/juventudes/): conteúdo complementar coletado com Selenium.

## Links do Projeto

- [Aplicação publicada no Streamlit Community Cloud](https://empregabilidade-jovem-renan-tp3.streamlit.app/)
- [Repositório no GitHub](https://github.com/renanvolcofnunes/Renan_VolcofNunes_PB_TP3)

O TP3 reúne o dashboard, as coletas e a integração HTTP local como base para a continuidade do projeto no TP4.
