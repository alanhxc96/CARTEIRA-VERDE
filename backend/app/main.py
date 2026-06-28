# -*- coding: utf-8 -*-
"""
Carteira Verde, backend (FastAPI).

API de demonstracao do haCARthon. Serve, com dados simulados:
  - login do gov.br (simulado, sem conexao real)
  - dados do imovel do produtor de exemplo (Seu Raimundo)
  - beneficios a que ele tem direito
  - regras que variam por estado, com as leis de referencia
  - os cinco perfis-tipo da porta generica

Nada aqui e dado real e nada e gravado: tudo vive em memoria, so para alimentar
a interface. Documentacao interativa em /docs.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, imovel, estados, perfis

app = FastAPI(
    title="Carteira Verde API",
    description="Backend de demonstracao do haCARthon. Dados de Cadastro Ambiental Rural e login gov.br sao simulados.",
    version="1.0.0",
)

# Libera o acesso da interface (em um demo, permitimos qualquer origem).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(imovel.router)
app.include_router(estados.router)
app.include_router(perfis.router)


@app.get("/", tags=["Saúde"], summary="Informações da API")
def raiz():
    """Pagina inicial da API, com a lista de rotas e um lembrete de que tudo e simulado."""
    return {
        "projeto": "Carteira Verde",
        "descricao": "Backend de demonstracao do haCARthon. Todos os dados sao ficticios.",
        "documentacao": "/docs",
        "rotas": {
            "login_simulado": "POST /api/login",
            "imovel_do_raimundo": "GET /api/imovel",
            "beneficios_do_raimundo": "GET /api/beneficios",
            "regras_por_estado": "GET /api/estados e GET /api/estados/{uf}",
            "fontes_legais": "GET /api/fontes-legais",
            "perfis_tipo": "GET /api/perfis e GET /api/perfis/{perfil_id}",
            "saude": "GET /saude",
        },
    }


@app.get("/saude", tags=["Saúde"], summary="Checagem de saúde")
def saude():
    """Responde se a API esta no ar."""
    return {"status": "ok"}
