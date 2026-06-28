# -*- coding: utf-8 -*-
"""Modelos de dados (Pydantic) usados nas respostas da API."""

from typing import List, Optional
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    cpf: str = Field(..., example="123.456.789-09")
    senha: str = Field(..., example="senhademonstracao")


class LoginResponse(BaseModel):
    autenticado: bool
    token: str
    nome: str
    cpf: str
    aviso: str


class Imovel(BaseModel):
    nome: str
    municipio: str
    uf: str
    area_ha: float
    modulos_fiscais: float
    porte: str
    bioma: str
    reserva_legal_exigida_percent: float
    reserva_legal_exigida_ha: float
    mata_nativa_ha: float
    excedente_ha: float
    app_situacao: str
    situacao_cadastro: str
    numero_cadastro: str


class ImovelResponse(BaseModel):
    nome: str
    cpf: str
    imovel: Imovel


class Beneficio(BaseModel):
    id: str
    titulo: str
    descricao: str
    primeiro_passo: str
    base_legal: str


class FonteLegal(BaseModel):
    titulo: str
    descricao: str
    url: str


class Estado(BaseModel):
    uf: str
    nome: str
    bioma: str
    reserva_legal: str
    modulo_fiscal: str
    programa_regularizacao: str
    orgao_ambiental: str
    site_orgao: str
    alerta: str
    itens: List[str]
    fontes_legais: Optional[List[FonteLegal]] = None


class PerfilCard(BaseModel):
    titulo: str
    texto: str
    base_legal: str


class Perfil(BaseModel):
    id: str
    titulo: str
    resumo: str
    cards: List[PerfilCard]
