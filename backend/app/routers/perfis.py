# -*- coding: utf-8 -*-
"""Perfis-tipo da porta generica (qual desses e voce), sem login."""

from typing import List
from fastapi import APIRouter, HTTPException
from ..models import Perfil
from .. import data

router = APIRouter(prefix="/api", tags=["Perfis"])


@router.get("/perfis", response_model=List[Perfil], summary="Os cinco perfis-tipo")
def listar_perfis():
    """Lista os cinco perfis e a carteira de beneficios em tese de cada um."""
    return list(data.PERFIS.values())


@router.get("/perfis/{perfil_id}", response_model=Perfil, summary="Um perfil específico")
def get_perfil(perfil_id: str):
    """Devolve um perfil pelo identificador (mata, recuperar, vender, comecando, emdia)."""
    perfil = data.PERFIS.get(perfil_id.lower())
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil nao encontrado. Use: mata, recuperar, vender, comecando ou emdia.")
    return perfil
