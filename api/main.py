import csv
from pathlib import Path
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(title="API de Empregabilidade Jovem no Brasil", description="API para consulta dos indicadores e envio de notícias do projeto.", version="1.0")

BASE = Path(__file__).resolve().parent.parent
ARQUIVO = BASE / "data" / "sample" / "empregabilidade_jovem.csv"
ARQUIVO_NOTICIAS_API = BASE / "data" / "processed" / "noticias_api.csv"

class NoticiaEntrada(BaseModel):
    titulo: str = Field(min_length=1)
    data: str = Field(min_length=1)
    url: HttpUrl
    fonte: str = Field(min_length=1)

def carregar_dados():
    dados = []

    with open(ARQUIVO, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha["taxa_desocupacao"] = float(linha["taxa_desocupacao"])
            dados.append(linha)

    return dados

def carregar_noticias_api():
    noticias = []

    if ARQUIVO_NOTICIAS_API.exists():
        with open(ARQUIVO_NOTICIAS_API, "r", encoding="utf-8-sig") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                noticias.append(linha)

    return noticias

@app.get("/", summary="Início")
def inicio():
    return {"mensagem": "API de Empregabilidade Jovem no Brasil"}

@app.get("/indicadores", summary="Consultar indicadores")
def indicadores(regiao: str | None = Query(default=None)):
    dados = carregar_dados()

    if regiao is not None:
        dados = [linha for linha in dados if linha["regiao"].lower() == regiao.lower()]

    return {"quantidade": len(dados), "dados": dados}

@app.get("/indicadores/{uf}", summary="Consultar indicador por UF")
def indicador_uf(uf: str):
    dados = carregar_dados()
    resultado = [linha for linha in dados if linha["uf"].upper() == uf.upper()]

    return {"uf": uf.upper(), "quantidade": len(resultado), "dados": resultado}

@app.get("/noticias", summary="Consultar notícias enviadas pela API")
def listar_noticias():
    noticias = carregar_noticias_api()

    return {"quantidade": len(noticias), "dados": noticias}

@app.post("/noticias", summary="Enviar nova notícia", status_code=201)
def adicionar_noticia(noticia: NoticiaEntrada):
    ARQUIVO_NOTICIAS_API.parent.mkdir(parents=True, exist_ok=True)
    arquivo_novo = not ARQUIVO_NOTICIAS_API.exists() or ARQUIVO_NOTICIAS_API.stat().st_size == 0

    with open(ARQUIVO_NOTICIAS_API, "a", encoding="utf-8-sig", newline="") as arquivo:
        campos = ["titulo", "data", "url", "fonte"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if arquivo_novo:
            escritor.writeheader()

        escritor.writerow({"titulo": noticia.titulo, "data": noticia.data, "url": str(noticia.url), "fonte": noticia.fonte})

    return {"mensagem": "Notícia adicionada com sucesso.", "dados": {"titulo": noticia.titulo, "data": noticia.data, "url": str(noticia.url), "fonte": noticia.fonte}}