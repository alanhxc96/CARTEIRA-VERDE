# -*- coding: utf-8 -*-
"""Regras que variam por estado, com as leis de onde vem cada informacao."""

from typing import List
from fastapi import APIRouter, HTTPException
from ..models import Estado, FonteLegal
from .. import data

router = APIRouter(prefix="/api", tags=["Estados"])


@router.get("/estados", response_model=List[Estado], summary="Regras de todos os estados")
def listar_estados():
    """Lista as regras de Reserva Legal, modulo fiscal, orgao e programa de cada estado."""
    return [_com_fontes(e) for e in data.ESTADOS.values()]


@router.get("/estados/{uf}", response_model=Estado, summary="Regras de um estado")
def get_estado(uf: str):
    """Devolve as regras de um estado pela sigla (ex.: sp, mg, pa)."""
    estado = data.ESTADOS.get(uf.lower())
    if not estado:
        raise HTTPException(status_code=404, detail="Estado nao encontrado. Use a sigla, por exemplo: sp, mg, pa.")
    return _com_fontes(estado)


@router.get("/fontes-legais", response_model=List[FonteLegal], summary="Leis de onde vêm as regras")
def fontes_legais():
    """Lista as leis oficiais de onde vem as regras, para a pessoa conferir na fonte."""
    return data.FONTES_LEGAIS


def _com_fontes(estado: dict) -> dict:
    """Anexa as fontes legais a cada estado, para a pessoa poder conferir."""
    return {**estado, "fontes_legais": data.FONTES_LEGAIS}
