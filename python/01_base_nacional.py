import pandas as pd
from pathlib import Path


# ============================================================
# BET ANALYTICS
# BETS NO BRASIL
# BASE NACIONAL - 2025 / 2026
#
# IMPORTANTE:
# - Não há dados de 2024 nesta base.
# - Não existem registros individuais fictícios.
# - Cada linha representa um indicador agregado publicado
#   por uma fonte identificada.
# ============================================================


# ============================================================
# 1. CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 2. DADOS
# ============================================================
dados = [

    # ========================================================
    # MERCADO REGULADO
    # 1º SEMESTRE DE 2025
    # Fonte: TCU / Ministério da Fazenda
    # ========================================================

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "TCU / Ministério da Fazenda",
        "tema": "Mercado",
        "indicador": "Apostadores em operadores autorizados",
        "valor": 17_700_000,
        "unidade": "pessoas",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Brasileiros que realizaram apostas em operadores "
            "autorizados no primeiro semestre de 2025."
        )
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "TCU / Ministério da Fazenda",
        "tema": "Mercado",
        "indicador": "Receita bruta do mercado regulado (GGR)",
        "valor": 17_400_000_000,
        "unidade": "R$",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "GGR: diferença entre os valores apostados "
            "e os prêmios pagos aos jogadores."
        )
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "TCU / Ministério da Fazenda",
        "tema": "Mercado",
        "indicador": "Tributos federais arrecadados",
        "valor": 3_800_000_000,
        "unidade": "R$",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Arrecadação federal relacionada ao setor no "
            "primeiro semestre de 2025."
        )
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "TCU / Ministério da Fazenda",
        "tema": "Mercado",
        "indicador": "Destinações sociais",
        "valor": 2_140_000_000,
        "unidade": "R$",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Destinações previstas na legislação das apostas."
        )
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "TCU / Ministério da Fazenda",
        "tema": "Comportamento financeiro",
        "indicador": "Gasto efetivo médio mensal por apostador",
        "valor": 164,
        "unidade": "R$/mês",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Média estimada a partir do gasto efetivo "
            "dos apostadores ativos."
        )
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "TCU / Ministério da Fazenda",
        "tema": "Comportamento financeiro",
        "indicador": "Gasto efetivo médio semestral por apostador",
        "valor": 983,
        "unidade": "R$/semestre",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Valor médio informado para apostadores ativos."
        )
    },


    # ========================================================
    # PERFIL DOS APOSTADORES
    # 1º SEMESTRE DE 2025
    # ========================================================

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Perfil",
        "indicador": "Apostadores homens",
        "valor": 71.0,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Distribuição por sexo dos apostadores."
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Perfil",
        "indicador": "Apostadores mulheres",
        "valor": 28.9,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Distribuição por sexo dos apostadores."
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Perfil",
        "indicador": "Apostadores de 18 a 25 anos",
        "valor": 22.4,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Faixa etária."
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Perfil",
        "indicador": "Apostadores de 25 a 30 anos",
        "valor": 22.2,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Faixa etária."
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Perfil",
        "indicador": "Apostadores de 31 a 40 anos",
        "valor": 27.8,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Faixa etária."
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Perfil",
        "indicador": "Apostadores de 41 a 50 anos",
        "valor": 16.9,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Faixa etária."
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Perfil",
        "indicador": "Apostadores de 51 a 60 anos",
        "valor": 7.8,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Faixa etária."
    },

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Perfil",
        "indicador": "Apostadores de 61 a 70 anos",
        "valor": 2.1,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Faixa etária."
    },


    # ========================================================
    # FISCALIZAÇÃO
    # 1º SEMESTRE DE 2025
    # ========================================================

    {
        "ano": 2025,
        "periodo": "1º semestre",
        "fonte": "Ministério da Fazenda / SPA",
        "tema": "Mercado ilegal",
        "indicador": "Páginas de apostas retiradas do ar",
        "valor": 15463,
        "unidade": "páginas",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Páginas retiradas do ar pela Anatel desde "
            "outubro de 2024 até o fim do primeiro semestre de 2025."
        )
    },


    # ========================================================
    # BOLSA FAMÍLIA
    # JANEIRO DE 2025
    # ========================================================

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Transferências para apostas online",
        "valor": 3_698_000_000,
        "unidade": "R$",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Transferências identificadas para contas de "
            "operadores de apostas por indivíduos identificados "
            "como beneficiários do programa."
        )
    },

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Famílias que fizeram transferências",
        "valor": 4_440_000,
        "unidade": "famílias",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Aproximadamente 21,9% das famílias analisadas."
        )
    },

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Famílias com até 2% da renda comprometida",
        "valor": 81.97,
        "unidade": "%",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Cálculo considerando renda total e retorno de "
            "85% dos valores apostados aos ganhadores."
        )
    },

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Famílias com mais de 2% da renda comprometida",
        "valor": 18.03,
        "unidade": "%",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "O TCU classificou esse grupo como situação crítica "
            "de comprometimento de necessidades básicas e alto risco social."
        )
    },

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Famílias com mais de 2% da renda comprometida",
        "valor": 801962,
        "unidade": "famílias",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": "Número informado pelo TCU."
    },

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Famílias com até 2% da renda comprometida",
        "valor": 3645162,
        "unidade": "famílias",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": "Número informado pelo TCU."
    },

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Famílias com renda própria declarada",
        "valor": 83.93,
        "unidade": "%",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Importante para interpretar a origem dos recursos."
        )
    },

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Famílias responsáveis por 80% das transferências",
        "valor": 4.37,
        "unidade": "%",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Pequena parcela das famílias concentrou cerca de "
            "80% do montante transferido."
        )
    },

    {
        "ano": 2025,
        "periodo": "Janeiro",
        "fonte": "TCU",
        "tema": "Bolsa Família",
        "indicador": "Benefício médio familiar",
        "valor": 673.90,
        "unidade": "R$",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": "Valor médio informado pelo TCU."
    },


    # ========================================================
    # ENDIVIDAMENTO / CRÉDITO
    # ESTUDO INSPER + STONE - 2026
    # ========================================================

    {
        "ano": 2026,
        "periodo": "Estudo publicado em setembro",
        "fonte": "Insper + Stone",
        "tema": "Endividamento",
        "indicador": "Aumento da inadimplência após início das apostas",
        "valor": 20.0,
        "unidade": "%",
        "tipo_dado": "efeito estimado",
        "abrangencia": "Brasil",
        "observacao": (
            "Comparação entre novos apostadores e grupo de comparação. "
            "O estudo acompanha os 12 meses seguintes à primeira aposta."
        )
    },

    {
        "ano": 2026,
        "periodo": "Estudo publicado em setembro",
        "fonte": "Insper + Stone",
        "tema": "Crédito",
        "indicador": "Aumento na dívida/atraso de cartão",
        "valor": 38.7,
        "unidade": "%",
        "tipo_dado": "efeito estimado",
        "abrangencia": "Brasil",
        "observacao": (
            "Variação estimada no primeiro ano após o início das apostas."
        )
    },

    {
        "ano": 2026,
        "periodo": "Estudo publicado em setembro",
        "fonte": "Insper + Stone",
        "tema": "Crédito",
        "indicador": "Redução do acesso ao crédito",
        "valor": -16.0,
        "unidade": "%",
        "tipo_dado": "efeito estimado",
        "abrangencia": "Brasil",
        "observacao": (
            "Redução observada/estimada no limite de crédito "
            "em comparação com o grupo de controle."
        )
    },

    {
        "ano": 2026,
        "periodo": "Estudo publicado em setembro",
        "fonte": "Insper + Stone",
        "tema": "Perfil",
        "indicador": "População aproximada considerada no estudo",
        "valor": 25_000_000,
        "unidade": "pessoas",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Estimativa de pessoas que apostam utilizada no contexto "
            "do estudo."
        )
    },


    # ========================================================
    # INADIMPLÊNCIA
    # SICREDI - 2026
    # ========================================================

    {
        "ano": 2026,
        "periodo": "Dados de julho",
        "fonte": "Sicredi",
        "tema": "Endividamento",
        "indicador": "Inadimplência maior entre apostadores",
        "valor": 40.0,
        "unidade": "%",
        "tipo_dado": "associação observada",
        "abrangencia": "Amostra nacional do Sicredi",
        "observacao": (
            "Inadimplência 40% maior entre associados que "
            "apostaram em 2025, em comparação aos que não apostaram."
        )
    },

    {
        "ano": 2026,
        "periodo": "Julho",
        "fonte": "Sicredi",
        "tema": "Endividamento",
        "indicador": "Pessoas analisadas no estudo",
        "valor": 1_300_000,
        "unidade": "pessoas",
        "tipo_dado": "amostra",
        "abrangencia": "Associados Sicredi",
        "observacao": (
            "Pessoas físicas com operações de crédito ativas."
        )
    },


    # ========================================================
    # MERCADO ILEGAL
    # TCU - 2026
    # ========================================================

    {
        "ano": 2026,
        "periodo": "Maio",
        "fonte": "TCU",
        "tema": "Mercado ilegal",
        "indicador": "Participação estimada do mercado ilegal - mínimo",
        "valor": 41.0,
        "unidade": "%",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Estimativa de participação dos operadores ilegais "
            "no volume total de apostas."
        )
    },

    {
        "ano": 2026,
        "periodo": "Maio",
        "fonte": "TCU",
        "tema": "Mercado ilegal",
        "indicador": "Participação estimada do mercado ilegal - máximo",
        "valor": 51.0,
        "unidade": "%",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Estimativa de participação dos operadores ilegais "
            "no volume total de apostas."
        )
    },

    {
        "ano": 2026,
        "periodo": "Maio",
        "fonte": "TCU",
        "tema": "Mercado ilegal",
        "indicador": "Volume anual potencial do mercado ilegal",
        "valor": 40_000_000_000,
        "unidade": "R$/ano",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "O TCU indica que a atividade ilegal pode corresponder "
            "a até aproximadamente R$ 40 bilhões anuais."
        )
    },


    # ========================================================
    # SAÚDE PÚBLICA
    # DADO CITADO PELO TCU EM 2026
    # ========================================================

    {
        "ano": 2026,
        "periodo": "Últimos cinco anos",
        "fonte": "TCU / IEPS",
        "tema": "Saúde",
        "indicador": "Aumento da busca por atendimento no SUS",
        "valor": 140.0,
        "unidade": "%",
        "tipo_dado": "variação observada",
        "abrangencia": "Brasil",
        "observacao": (
            "Aumento informado pelo TCU em atendimentos/buscas "
            "relacionados a problemas de jogo."
        )
    },

    {
        "ano": 2026,
        "periodo": "Estimativa anual",
        "fonte": "TCU / IEPS",
        "tema": "Saúde",
        "indicador": "Impacto anual estimado na saúde pública",
        "valor": 30_000_000_000,
        "unidade": "R$/ano",
        "tipo_dado": "estimativa",
        "abrangencia": "Brasil",
        "observacao": (
            "Estimativa citada pelo TCU com base em estudo do IEPS. "
            "Inclui despesas associadas a depressão, ansiedade e "
            "impactos relacionados a mortes por suicídio."
        )
    },


    # ========================================================
    # FISCALIZAÇÃO - 2026
    # MINISTÉRIO DA JUSTIÇA / FAZENDA
    # ========================================================

    {
        "ano": 2026,
        "periodo": "27 de setembro",
        "fonte": "Ministério da Justiça e Segurança Pública / Ministério da Fazenda",
        "tema": "Mercado ilegal",
        "indicador": "Sites suspeitos de apostas derrubados",
        "valor": 506,
        "unidade": "sites",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Domínios com indícios de oferta irregular de apostas."
        )
    },

    {
        "ano": 2026,
        "periodo": "25 a 27 de setembro",
        "fonte": "Ministério da Justiça e Segurança Pública",
        "tema": "Publicidade ilegal",
        "indicador": "Anúncios suspeitos identificados no Google",
        "valor": 1960,
        "unidade": "anúncios",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Anúncios relacionados a sete domínios exibidos "
            "no Brasil no período monitorado."
        )
    },

    {
        "ano": 2026,
        "periodo": "27 de setembro",
        "fonte": "Ministério da Justiça e Segurança Pública",
        "tema": "Publicidade ilegal",
        "indicador": "Canais e grupos de apostas identificados no Telegram",
        "valor": 43,
        "unidade": "canais/grupos",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Canais e grupos relacionados à divulgação de apostas "
            "e jogos de cassino online."
        )
    },

    {
        "ano": 2026,
        "periodo": "27 de setembro",
        "fonte": "Ministério da Justiça e Segurança Pública",
        "tema": "Publicidade ilegal",
        "indicador": "Membros na rede de divulgação identificada no Telegram",
        "valor": 212_000,
        "unidade": "membros",
        "tipo_dado": "observado",
        "abrangencia": "Brasil",
        "observacao": (
            "Rede de divulgação de apostas identificada pelo Ciberlab."
        )
    },


    # ========================================================
    # DATASENADO - PESQUISA NACIONAL 2025
    #
    # CONTEXTO SOCIAL SOBRE JOGOS E APOSTAS.
    # NÃO representa percentual de apostadores.
    # ========================================================

    {
        "ano": 2025,
        "periodo": "21/02 a 01/03",
        "fonte": "DataSenado",
        "tema": "Percepção social",
        "indicador": "Brasileiros que consideram importante evitar endividamento com jogos",
        "valor": 77.0,
        "unidade": "%",
        "tipo_dado": "pesquisa de opinião",
        "abrangencia": "Brasil",
        "observacao": (
            "Pesquisa nacional com 5.039 entrevistados. "
            "Pergunta relacionada a jogos, não exclusivamente às bets."
        )
    },

    {
        "ano": 2025,
        "periodo": "21/02 a 01/03",
        "fonte": "DataSenado",
        "tema": "Percepção social",
        "indicador": "Brasileiros que consideram importante combater lavagem de dinheiro em jogos",
        "valor": 82.0,
        "unidade": "%",
        "tipo_dado": "pesquisa de opinião",
        "abrangencia": "Brasil",
        "observacao": (
            "Pesquisa nacional com 5.039 entrevistados."
        )
    },

    {
        "ano": 2025,
        "periodo": "21/02 a 01/03",
        "fonte": "DataSenado",
        "tema": "Percepção social",
        "indicador": "Brasileiros que avaliam positivamente cadastro de pessoas com vício em jogos",
        "valor": 54.0,
        "unidade": "%",
        "tipo_dado": "pesquisa de opinião",
        "abrangencia": "Brasil",
        "observacao": (
            "Pesquisa nacional com 5.039 entrevistados."
        )
    }
]


# ============================================================
# 3. DATAFRAME
# ============================================================

df = pd.DataFrame(dados)


# ============================================================
# 4. GARANTIA: NENHUM REGISTRO DE 2024
# ============================================================

if 2024 in df["ano"].unique():
    raise ValueError(
        "ERRO: foi encontrado dado de 2024 na base."
    )


# ============================================================
# 5. DATA DE REFERÊNCIA COMO TEXTO
# ============================================================

df["ano"] = df["ano"].astype(int)


# ============================================================
# 6. ORDENAÇÃO
# ============================================================

df = df.sort_values(
    by=[
        "ano",
        "tema",
        "indicador"
    ]
).reset_index(drop=True)


# ============================================================
# 7. EXPORTAR CSV
# ============================================================

arquivo_csv = (
    PROCESSED_DIR /
    "bets_brasil_2025_2026.csv"
)

df.to_csv(
    arquivo_csv,
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# 8. RESUMO POR TEMA
# ============================================================

resumo_tema = (
    df.groupby(
        ["ano", "tema"],
        as_index=False
    )
    .size()
    .rename(
        columns={
            "size": "quantidade_indicadores"
        }
    )
)

arquivo_resumo = (
    PROCESSED_DIR /
    "resumo_temas_bets.csv"
)

resumo_tema.to_csv(
    arquivo_resumo,
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# 9. RESUMO NO TERMINAL
# ============================================================

print()
print("=" * 75)
print("BET ANALYTICS")
print("BASE NACIONAL - 2025 / 2026")
print("=" * 75)

print()
print(f"Total de indicadores: {len(df)}")

print()
print("Anos:")
print(
    df["ano"]
    .value_counts()
    .sort_index()
)

print()
print("Temas:")
print(
    df["tema"]
    .value_counts()
)

print()
print("Fontes:")
print(
    df["fonte"]
    .value_counts()
)

print()
print("=" * 75)
print("PRINCIPAIS INDICADORES")
print("=" * 75)

for _, linha in df.iterrows():

    print(
        f"{linha['ano']} | "
        f"{linha['tema']} | "
        f"{linha['indicador']} | "
        f"{linha['valor']} "
        f"{linha['unidade']}"
    )


# ============================================================
# 10. ARQUIVOS GERADOS
# ============================================================

print()
print("=" * 75)
print("ARQUIVOS GERADOS")
print("=" * 75)

print(arquivo_csv)
print(arquivo_resumo)

print()
print("Processamento concluído.")
print("=" * 75)