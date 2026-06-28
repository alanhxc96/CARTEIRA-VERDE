# Carteira Verde

Projeto do haCARthon (Desafio 3). A Carteira Verde traduz a lei ambiental rural
em beneficios que o produtor entende. Em vez de mostrar o que a lei obriga, ela
mostra o que a lei da: credito mais barato, isencao de imposto, renda da mata em
pe, seguranca juridica.

A pessoa escolhe um perfil que parece com a terra dela e ja ve, sem login, os
beneficios em tese. Depois, entrando com a conta gov.br (simulada), ve os dados
do proprio imovel e os beneficios especificos a que tem direito.

Importante: o login do gov.br e simulado e os dados do Cadastro Ambiental Rural
sao ficticios. Tudo e para demonstracao do hackathon.

## Estrutura

```
.
├── index.html        interface atual da Carteira Verde (front, roda sozinha)
├── backend/          API de demonstracao em FastAPI (ver backend/README.md)
└── portal-car-v5.html   versao anterior da interface (historico)
```

- A interface (`index.html`) e um arquivo unico, sem dependencia de servidor, que
  funciona offline. E o que vai na gravacao do pitch.
- O backend (`backend/`) e uma API FastAPI que serve os mesmos dados (imovel,
  beneficios, estados, perfis) de forma simulada, com documentacao automatica em
  `/docs`. Ele da robustez tecnica ao projeto e abre o caminho para uma integracao
  real no futuro.

## Rodando

Interface: abra `index.html` no navegador.

Backend: veja as instrucoes em [backend/README.md](backend/README.md). Em resumo:

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# documentacao em http://127.0.0.1:8000/docs
```

## Fontes das regras

As regras de Reserva Legal, modulo fiscal e regularizacao vem da legislacao
federal e dos dados oficiais, e os links de conferencia acompanham cada estado:

- Codigo Florestal (Lei 12.651/2012)
- Decreto 7.830/2012 (Cadastro Ambiental Rural e Programa de Regularizacao Ambiental)
- Modulo fiscal por municipio (INCRA)
