# -*- coding: utf-8 -*-
"""Dados do imovel e dos beneficios do produtor de exemplo (Seu Raimundo)."""

from typing import List
from fastapi import APIRouter
from ..models import ImovelResponse, Beneficio
from .. import data

router = APIRouter(prefix="/api", tags=["Imóvel e benefícios (simulado)"])


@router.get("/imovel", response_model=ImovelResponse, summary="Dados do imóvel do Seu Raimundo")
def get_imovel():
    """Devolve os dados ficticios do imovel do Seu Raimundo no Cadastro Ambiental Rural."""
    return ImovelResponse(nome=data.RAIMUNDO["nome"], cpf=data.RAIMUNDO["cpf"], imovel=data.RAIMUNDO["imovel"])


@router.get("/beneficios", response_model=List[Beneficio], summary="Benefícios a que o Seu Raimundo tem direito")
def get_beneficios():
    """Lista os beneficios calculados a partir do perfil do imovel do Seu Raimundo."""
    return data.BENEFICIOS_RAIMUNDO
