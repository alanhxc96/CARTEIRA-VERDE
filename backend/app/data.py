# -*- coding: utf-8 -*-
"""
Dados simulados da Carteira Verde.

O login do gov.br e os dados do Cadastro Ambiental Rural aqui sao ficticios,
usados apenas para demonstracao no haCARthon. Nenhum dado e real e nada e
gravado: tudo vive em memoria, so para alimentar a interface.
"""

# ───────────────────────── Produtor de exemplo (Seu Raimundo) ─────────────────────────
RAIMUNDO = {
    "nome": "Raimundo Silva",
    "cpf": "123.456.789-09",
    "imovel": {
        "nome": "Sítio Boa Esperança",
        "municipio": "Acaiaca",
        "uf": "MG",
        "area_ha": 48,
        "modulos_fiscais": 2.4,
        "porte": "Pequeno",
        "bioma": "Mata Atlântica",
        "reserva_legal_exigida_percent": 20,
        "reserva_legal_exigida_ha": 9.6,
        "mata_nativa_ha": 18,
        "excedente_ha": 8.4,
        "app_situacao": "Faixa de rio preservada",
        "situacao_cadastro": "Cadastro ativo",
        "numero_cadastro": "MG-3100401-A1B2.C3D4.E5F6",
    },
}

# Benefícios a que o Seu Raimundo tem direito, calculados a partir do perfil do imóvel
# (preserva mata nativa além do mínimo, está regular, é pequeno produtor).
BENEFICIOS_RAIMUNDO = [
    {
        "id": "cra",
        "titulo": "Floresta que vira renda",
        "descricao": "Você tem cerca de 8 hectares de mata além do mínimo. Esse excedente pode virar Cota de Reserva Ambiental e ser vendido para quem precisa compensar.",
        "primeiro_passo": "Peça ao órgão ambiental a análise do seu excedente de mata.",
        "base_legal": "Art. 44 da Lei 12.651/2012",
    },
    {
        "id": "psa",
        "titulo": "Receber para conservar",
        "descricao": "Por manter 18 hectares de mata e proteger a nascente, você pode receber por conservar, através do Pagamento por Serviços Ambientais.",
        "primeiro_passo": "Procure os programas de Pagamento por Serviços Ambientais do seu estado.",
        "base_legal": "Lei 14.119/2021",
    },
    {
        "id": "itr",
        "titulo": "Imposto que você deixa de pagar",
        "descricao": "Os 18 hectares de mata e as áreas de preservação ficam livres do Imposto Territorial Rural.",
        "primeiro_passo": "Declare essas áreas na sua declaração do Imposto Territorial Rural.",
        "base_legal": "Art. 10 da Lei 9.393/1996",
    },
    {
        "id": "credito",
        "titulo": "Crédito mais barato",
        "descricao": "Com o cadastro ativo, você acessa crédito rural com juros melhores no Banco do Brasil, Sicredi, Caixa e cooperativas.",
        "primeiro_passo": "Leve o comprovante do cadastro ativo ao seu banco ou cooperativa.",
        "base_legal": "Resolução Bacen 4.106/2012",
    },
    {
        "id": "juridico",
        "titulo": "Segurança jurídica",
        "descricao": "Seu imóvel fica protegido de embargos e impedimentos que travam a produção e a venda.",
        "primeiro_passo": "Guarde o comprovante do cadastro ativo do seu imóvel.",
        "base_legal": "Art. 2º, §2º, da Lei 12.651/2012",
    },
]

# ───────────────────────── Leis de onde vêm as regras ─────────────────────────
FONTES_LEGAIS = [
    {
        "titulo": "Código Florestal (Lei 12.651/2012)",
        "descricao": "Define a Reserva Legal por bioma (Art. 12) e as Áreas de Preservação Permanente.",
        "url": "https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12651.htm",
    },
    {
        "titulo": "Decreto 7.830/2012",
        "descricao": "Cria o Cadastro Ambiental Rural e o Programa de Regularização Ambiental.",
        "url": "https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/decreto/d7830.htm",
    },
    {
        "titulo": "Módulo fiscal (INCRA)",
        "descricao": "O módulo fiscal de cada município é definido pelo INCRA.",
        "url": "https://www.gov.br/incra/pt-br/assuntos/governanca-fundiaria/modulo-fiscal",
    },
]

# ───────────────────────── Regras por estado (10 exemplos) ─────────────────────────
ESTADOS = {
    "pa": {
        "uf": "PA", "nome": "Pará", "bioma": "Amazônia Legal",
        "reserva_legal": "80%", "modulo_fiscal": "70 ha", "programa_regularizacao": "Disponível",
        "orgao_ambiental": "SEMAS-PA", "site_orgao": "https://www.semas.pa.gov.br",
        "alerta": "Fiscalização federal forte: vale regularizar o quanto antes.",
        "itens": [
            "Floresta amazônica: Reserva Legal de 80% da propriedade",
            "Módulo fiscal médio de 70 hectares (varia por município)",
            "O órgão ambiental do estado oferece apoio técnico gratuito aos pequenos produtores",
            "Programa de Regularização Ambiental ativo e regulamentado",
            "Cadastro estadual integrado ao sistema nacional do Cadastro Ambiental Rural",
        ],
    },
    "mt": {
        "uf": "MT", "nome": "Mato Grosso", "bioma": "Amazônia + Cerrado + Pantanal",
        "reserva_legal": "80% / 35% / 35%", "modulo_fiscal": "65 ha", "programa_regularizacao": "Regulamentado",
        "orgao_ambiental": "SEMA-MT", "site_orgao": "https://www.sema.mt.gov.br",
        "alerta": "Confirme o bioma exato: Mato Grosso tem três biomas diferentes.",
        "itens": [
            "Reserva Legal por bioma: floresta amazônica 80%, Cerrado 35%, Pantanal 35%",
            "Módulo fiscal médio de 65 hectares",
            "Confirme o bioma da sua propriedade com o órgão ambiental do estado",
            "Programa de Regularização Ambiental regulamentado e integrado ao sistema nacional",
            "Cadastro Ambiental Rural obrigatório em todos os municípios",
        ],
    },
    "am": {
        "uf": "AM", "nome": "Amazonas", "bioma": "Amazônia Legal",
        "reserva_legal": "80% (pode ser 50%)", "modulo_fiscal": "100 ha", "programa_regularizacao": "Disponível",
        "orgao_ambiental": "SDS-AM", "site_orgao": "https://www.meioambiente.am.gov.br",
        "alerta": "A Reserva Legal pode cair para 50% se o município tiver mais da metade do território em Unidades de Conservação.",
        "itens": [
            "Floresta amazônica: Reserva Legal de 80% (pode ser 50% em casos especiais)",
            "Módulo fiscal médio de 100 hectares",
            "O órgão ambiental do estado oferece apoio técnico gratuito",
            "Apoio às comunidades ribeirinhas e aos pequenos produtores",
            "Cadastro estadual integrado ao sistema nacional do Cadastro Ambiental Rural",
        ],
    },
    "ro": {
        "uf": "RO", "nome": "Rondônia", "bioma": "Amazônia Legal",
        "reserva_legal": "80%", "modulo_fiscal": "60 ha", "programa_regularizacao": "Disponível",
        "orgao_ambiental": "SEDAM-RO", "site_orgao": "https://www.sedam.ro.gov.br",
        "alerta": "Região com histórico de desmatamento: a fiscalização é intensa.",
        "itens": [
            "Floresta amazônica: Reserva Legal de 80% da propriedade",
            "Módulo fiscal médio de 60 hectares",
            "O órgão ambiental do estado tem equipes no interior para apoio técnico",
            "Programa de Regularização Ambiental com foco em propriedades menores",
            "Cadastro estadual integrado ao sistema nacional do Cadastro Ambiental Rural",
        ],
    },
    "mg": {
        "uf": "MG", "nome": "Minas Gerais", "bioma": "Mata Atlântica / Cerrado",
        "reserva_legal": "20%", "modulo_fiscal": "20 ha", "programa_regularizacao": "Programa Regulariza MG",
        "orgao_ambiental": "SEMAD-MG", "site_orgao": "https://meioambiente.mg.gov.br",
        "alerta": "Mata Atlântica: áreas ocupadas antes de 2008 têm tratamento diferenciado.",
        "itens": [
            "Mata Atlântica e Cerrado: Reserva Legal de 20% da propriedade",
            "Módulo fiscal médio de 20 hectares",
            "Programa estadual Regulariza Minas em andamento",
            "O órgão ambiental do estado dá apoio técnico a propriedades de até 4 módulos fiscais",
            "Cadastro estadual de Minas integrado ao sistema nacional do Cadastro Ambiental Rural",
        ],
    },
    "sp": {
        "uf": "SP", "nome": "São Paulo", "bioma": "Mata Atlântica",
        "reserva_legal": "20%", "modulo_fiscal": "20 ha", "programa_regularizacao": "Disponível",
        "orgao_ambiental": "SMA-SP / CETESB", "site_orgao": "https://www.saopaulo.sp.gov.br/spnoticias/meio-ambiente",
        "alerta": "Mata Atlântica: há restrições adicionais nas faixas de preservação à beira de rios e nascentes.",
        "itens": [
            "Mata Atlântica: Reserva Legal de 20% da propriedade",
            "Módulo fiscal médio de 20 hectares",
            "O órgão ambiental do estado atende o produtor rural",
            "Programa de Regularização Ambiental com foco na Mata Atlântica",
            "Cadastro estadual de São Paulo integrado ao sistema nacional do Cadastro Ambiental Rural",
        ],
    },
    "go": {
        "uf": "GO", "nome": "Goiás", "bioma": "Cerrado",
        "reserva_legal": "35%", "modulo_fiscal": "25 ha", "programa_regularizacao": "Regulamentado",
        "orgao_ambiental": "SECIMA-GO", "site_orgao": "https://www.secima.go.gov.br",
        "alerta": "Cerrado é o bioma mais desmatado do Brasil: fiscalização crescente.",
        "itens": [
            "Cerrado: Reserva Legal de 35% da propriedade",
            "Módulo fiscal médio de 25 hectares",
            "O órgão ambiental do estado tem escritórios regionais",
            "Programa de Regularização Ambiental estadual regulamentado",
            "Cadastro estadual integrado ao sistema nacional do Cadastro Ambiental Rural",
        ],
    },
    "ba": {
        "uf": "BA", "nome": "Bahia", "bioma": "Caatinga / Cerrado / Mata Atlântica",
        "reserva_legal": "20% a 35%", "modulo_fiscal": "55 ha", "programa_regularizacao": "Disponível",
        "orgao_ambiental": "INEMA-BA", "site_orgao": "https://www.inema.ba.gov.br",
        "alerta": "A Bahia tem três biomas: confirme o bioma da sua área antes de declarar.",
        "itens": [
            "Três biomas: Caatinga 20%, Cerrado 35%, Mata Atlântica 20% de Reserva Legal",
            "Módulo fiscal médio de 55 hectares",
            "O órgão ambiental do estado tem atendimento regional",
            "Programa de Regularização Ambiental disponível para todos os biomas",
            "Atenção às faixas de preservação nos rios do semiárido",
        ],
    },
    "rs": {
        "uf": "RS", "nome": "Rio Grande do Sul", "bioma": "Pampa / Mata Atlântica",
        "reserva_legal": "20%", "modulo_fiscal": "18 ha", "programa_regularizacao": "Regulamentado",
        "orgao_ambiental": "SEMA-RS", "site_orgao": "https://www.sema.rs.gov.br",
        "alerta": "O Pampa é um bioma exclusivo do Brasil, com proteção específica.",
        "itens": [
            "Pampa e Mata Atlântica: Reserva Legal de 20% da propriedade",
            "Módulo fiscal médio de 18 hectares",
            "O órgão ambiental do estado apoia os produtores familiares",
            "Programa de Regularização Ambiental regulamentado, com foco no Pampa",
            "Cadastro estadual integrado ao sistema nacional do Cadastro Ambiental Rural",
        ],
    },
    "ms": {
        "uf": "MS", "nome": "Mato Grosso do Sul", "bioma": "Cerrado / Pantanal",
        "reserva_legal": "35%", "modulo_fiscal": "30 ha", "programa_regularizacao": "Disponível",
        "orgao_ambiental": "SEMADESC-MS", "site_orgao": "https://www.semadesc.ms.gov.br",
        "alerta": "Pantanal: há restrições adicionais a novas retiradas de vegetação.",
        "itens": [
            "Cerrado e Pantanal: Reserva Legal de 35% da propriedade",
            "Módulo fiscal médio de 30 hectares",
            "O órgão ambiental do estado dá atenção especial ao Pantanal",
            "Programa de Regularização Ambiental com foco na região pantaneira",
            "Cadastro estadual integrado ao sistema nacional do Cadastro Ambiental Rural",
        ],
    },
}

# ───────────────────────── Perfis-tipo da porta genérica ─────────────────────────
# Cada perfil abre uma carteira de benefícios em tese, sem login.
PERFIS = {
    "mata": {
        "id": "mata",
        "titulo": "Tenho mata nativa preservada",
        "resumo": "Você preserva mais mata do que a lei exige. Essa mata em pé pode virar dinheiro, e a lei te ajuda nisso.",
        "cards": [
            {"titulo": "Floresta que vira renda", "texto": "A mata que passa do mínimo exigido pode virar Cota de Reserva Ambiental e ser vendida para quem precisa compensar.", "base_legal": "Art. 44 da Lei 12.651/2012"},
            {"titulo": "Receber para conservar", "texto": "Programas de Pagamento por Serviços Ambientais pagam quem mantém mata nativa e protege nascentes.", "base_legal": "Lei 14.119/2021"},
            {"titulo": "Renda de carbono", "texto": "Floresta preservada gera crédito de carbono. Com o cadastro em dia, você pode entrar em projetos que pagam por isso.", "base_legal": "Lei 15.042/2024"},
            {"titulo": "Imposto que você deixa de pagar", "texto": "As áreas de mata e de preservação declaradas ficam livres do Imposto Territorial Rural.", "base_legal": "Art. 10 da Lei 9.393/1996"},
            {"titulo": "Crédito mais barato", "texto": "Bancos e cooperativas dão juros melhores para quem está regular.", "base_legal": "Resolução Bacen 4.106/2012"},
        ],
    },
    "recuperar": {
        "id": "recuperar",
        "titulo": "Desmatei e quero acertar",
        "resumo": "Você tem área para recuperar ou uma faixa de rio ocupada. A boa notícia: dá para acertar sem pagar multa, recuperando aos poucos.",
        "cards": [
            {"titulo": "Multa antiga suspensa", "texto": "Quem entra no Programa de Regularização Ambiental tem as multas antigas, de antes de 22 de julho de 2008, suspensas.", "base_legal": "Decreto 7.830/2012"},
            {"titulo": "Recuperar a beira do rio e as nascentes", "texto": "As Áreas de Preservação Permanente podem ser recompostas com apoio, dentro de um prazo combinado.", "base_legal": "Art. 4º e 61-A da Lei 12.651/2012"},
            {"titulo": "Saber quanto falta, sem susto", "texto": "A Reserva Legal é a parte da terra que precisa manter mata nativa. Saber o tamanho do que falta é o primeiro passo.", "base_legal": "Art. 12 da Lei 12.651/2012"},
            {"titulo": "Crédito de volta depois que você adere", "texto": "Ao assinar o compromisso de recuperação, você mantém o acesso ao crédito rural enquanto recupera.", "base_legal": "Art. 59 da Lei 12.651/2012"},
            {"titulo": "Segurança jurídica", "texto": "Com o cadastro ativo e o compromisso assinado, sua terra fica protegida de embargos.", "base_legal": "Art. 2º, §2º, da Lei 12.651/2012"},
        ],
    },
    "vender": {
        "id": "vender",
        "titulo": "Quero produzir e vender melhor",
        "resumo": "Estar regular abre portas de crédito, seguro e mercado que a terra irregular não alcança.",
        "cards": [
            {"titulo": "Crédito mais barato", "texto": "Regularidade ambiental virou condição para o crédito rural com juros menores.", "base_legal": "Resolução Bacen 4.106/2012"},
            {"titulo": "Seguro rural com prioridade", "texto": "O programa do governo que subsidia o seguro rural dá prioridade a quem está regular.", "base_legal": "Lei 10.823/2003"},
            {"titulo": "Financiamento da agricultura familiar e do médio produtor", "texto": "Os financiamentos da agricultura familiar e do médio produtor exigem regularidade ambiental.", "base_legal": "Resolução CMN 5.193/2024"},
            {"titulo": "Valorização da terra", "texto": "Imóvel regular vale mais, vende mais fácil e abre acesso a compradores que exigem rastreabilidade.", "base_legal": "Art. 29 da Lei 12.651/2012"},
        ],
    },
    "comecando": {
        "id": "comecando",
        "titulo": "Herdei ou estou começando agora",
        "resumo": "Calma: dá para fazer um passo de cada vez, com apoio gratuito do poder público.",
        "cards": [
            {"titulo": "Segurança para a sua terra", "texto": "O Cadastro Ambiental Rural organiza a situação do imóvel e protege contra embargos.", "base_legal": "Art. 2º, §2º, da Lei 12.651/2012"},
            {"titulo": "Entender quanto precisa preservar", "texto": "A Reserva Legal é a parte da terra que mantém mata nativa. O percentual muda conforme a região.", "base_legal": "Art. 12 da Lei 12.651/2012"},
            {"titulo": "As faixas de rio e nascentes", "texto": "Perto de rios, nascentes e encostas há faixas que a lei pede para preservar.", "base_legal": "Art. 4º da Lei 12.651/2012"},
            {"titulo": "Crédito e programas do governo", "texto": "Com o cadastro feito, você passa a poder acessar crédito rural e programas públicos.", "base_legal": "Resolução Bacen 4.106/2012"},
        ],
    },
    "emdia": {
        "id": "emdia",
        "titulo": "Já estou em dia",
        "resumo": "É hora de colher o que já é seu: menos imposto, crédito melhor e, se preserva mata, uma renda a mais.",
        "cards": [
            {"titulo": "Imposto que você deixa de pagar", "texto": "As áreas de preservação e de Reserva Legal declaradas ficam livres do Imposto Territorial Rural.", "base_legal": "Art. 10 da Lei 9.393/1996"},
            {"titulo": "Crédito mais barato", "texto": "Cadastro ativo garante as melhores condições de crédito rural.", "base_legal": "Resolução Bacen 4.106/2012"},
            {"titulo": "Segurança jurídica", "texto": "Sua terra fica protegida de embargos e impedimentos.", "base_legal": "Art. 2º, §2º, da Lei 12.651/2012"},
            {"titulo": "Se você preserva, pode vender o excedente", "texto": "A mata que passa do mínimo pode virar Cota de Reserva Ambiental e ser vendida.", "base_legal": "Art. 44 da Lei 12.651/2012"},
            {"titulo": "E pode receber para conservar", "texto": "Programas de Pagamento por Serviços Ambientais remuneram quem mantém mata nativa.", "base_legal": "Lei 14.119/2021"},
        ],
    },
}
