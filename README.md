# Empregabilidade Jovem no Brasil

Projeto desenvolvido para a disciplina Projeto de Bloco: Inteligência Artificial Aplicada.

O projeto analisa indicadores relacionados à empregabilidade de jovens no Brasil e reúne dados públicos, notícias e informações complementares sobre juventudes.

No TP3, a aplicação foi ampliada com navegação multipáginas, API FastAPI, integração entre Streamlit e API, coleta dinâmica com Selenium e preparação para futuras funcionalidades utilizando LLMs.

## Funcionalidades do TP3

- Navegação entre múltiplas páginas com Streamlit.
- Filtros de indicadores por região e estado.
- Comparação das taxas de desocupação entre estados.
- Visualização de tabelas e gráficos.
- Coleta de notícias com Requests e BeautifulSoup.
- Upload e validação de arquivos CSV.
- Análise de frequência das palavras presentes nos títulos das notícias.
- Download dos indicadores filtrados.
- API desenvolvida com FastAPI.
- Rotas GET para consulta de indicadores.
- Rota POST para envio de notícias.
- Integração entre Streamlit e FastAPI.
- Coleta dinâmica utilizando Selenium.
- Visualização dos dados coletados pelo Selenium.
- Preparação dos dados para futura utilização com LLMs.

## Estrutura do Projeto

- `app.py`: aplicação principal e navegação multipáginas.
- `comum.py`: funções e recursos compartilhados entre as páginas.
- `paginas/`: páginas da aplicação Streamlit.
- `api/main.py`: API desenvolvida com FastAPI.
- `src/data_access.py`: coleta de indicadores do IBGE.
- `src/coleta_web.py`: coleta de notícias utilizando Requests e BeautifulSoup.
- `src/coleta_dinamica.py`: coleta de dados utilizando Selenium.
- `data/sample/`: indicadores utilizados na aplicação.
- `data/raw/`: arquivos HTML obtidos durante a coleta Web.
- `data/processed/`: notícias e dados processados.
- `docs/project_charter.md`: Project Charter atualizado.
- `docs/data_summary_report.md`: Data Summary Report atualizado.
- `docs/metodologia_projeto.md`: metodologia utilizada no projeto.
- `requirements.txt`: dependências principais.
- `requirements-api.txt`: dependências da API.
- `requirements-coleta.txt`: dependências da coleta com Selenium.

## Ambiente de Desenvolvimento

### Criar o ambiente virtual

```powershell
python -m venv .venv