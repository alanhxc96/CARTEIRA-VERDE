# -*- coding: utf-8 -*-
"""
Login simulado do gov.br.

Atencao: isto NAO conecta no gov.br de verdade. E uma simulacao para a
demonstracao do haCARthon. Qualquer CPF e senha sao aceitos e a resposta
sempre traz o produtor de exemplo (Seu Raimundo).
"""

from fastapi import APIRouter
from ..models import LoginRequest, LoginResponse
from .. import data

router = APIRouter(prefix="/api", tags=["Login gov.br (simulado)"])


@router.post("/login", response_model=LoginResponse, summary="Login simulado do gov.br")
def login(req: LoginRequest):
    """Recebe CPF e senha e devolve um token ficticio. So para a demonstracao."""
    return LoginResponse(
        autenticado=True,
        token="demo-token-ficticio",
        nome=data.RAIMUNDO["nome"],
        cpf=req.cpf or data.RAIMUNDO["cpf"],
        aviso="Login simulado para demonstracao. Nao e o gov.br real.",
    )
