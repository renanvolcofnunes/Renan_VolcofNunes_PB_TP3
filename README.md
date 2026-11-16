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