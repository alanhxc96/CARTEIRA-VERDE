# Carteira Verde, backend

API de demonstracao do haCARthon, feita em FastAPI. Serve, com dados simulados,
o login do gov.br, os dados do imovel do produtor de exemplo (Seu Raimundo), os
beneficios a que ele tem direito, as regras que variam por estado e os cinco
perfis-tipo.

Importante: nada aqui e dado real. O login do gov.br e simulado (nao conecta no
gov.br de verdade) e os dados do Cadastro Ambiental Rural sao ficticios. Nada e
gravado: tudo vive em memoria, so para alimentar a interface.

## Como rodar

Precisa de Python 3.10 ou mais novo.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate          # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

A API sobe em http://127.0.0.1:8000.

Documentacao interativa (Swagger), onde da para testar cada rota pelo navegador:
http://127.0.0.1:8000/docs

## Rotas

| Metodo | Rota | O que faz |
|--------|------|-----------|
| GET  | `/` | Informacoes da API e lista de rotas |
| GET  | `/saude` | Responde se a API esta no ar |
| POST | `/api/login` | Login simulado do gov.br (qualquer CPF e senha sao aceitos) |
| GET  | `/api/imovel` | Dados do imovel do Seu Raimundo |
| GET  | `/api/beneficios` | Beneficios a que o Seu Raimundo tem direito |
| GET  | `/api/estados` | Regras de todos os estados |
| GET  | `/api/estados/{uf}` | Regras de um estado (ex.: `/api/estados/sp`) |
| GET  | `/api/fontes-legais` | Leis oficiais de onde vem as regras |
| GET  | `/api/perfis` | Os cinco perfis-tipo da porta generica |
| GET  | `/api/perfis/{perfil_id}` | Um perfil (mata, recuperar, vender, comecando, emdia) |

## Estrutura

```
backend/
  app/
    main.py            app FastAPI, CORS e rota de saude
    models.py          modelos das respostas (Pydantic)
    data.py            dados simulados (Raimundo, estados, perfis, beneficios)
    routers/
      auth.py          login simulado do gov.br
      imovel.py        imovel e beneficios do Raimundo
      estados.py       regras por estado e fontes legais
      perfis.py        perfis-tipo
  requirements.txt
```

## Como a interface se conecta (proximo passo)

Hoje a interface (../index.html) funciona sozinha, com a propria copia dos dados,
para rodar offline na gravacao do pitch. Os mesmos dados estao expostos por esta
API, entao ligar a interface ao backend e trocar os dados fixos por chamadas como:

```js
const r = await fetch("http://127.0.0.1:8000/api/imovel");
const dados = await r.json();
```

As fontes legais (Codigo Florestal, Decreto 7.830/2012 e modulo fiscal do INCRA)
acompanham cada estado em `fontes_legais`, para a pessoa poder conferir na fonte.
