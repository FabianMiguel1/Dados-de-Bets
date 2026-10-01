📊 Bets-Brasil: Análise de Dados, Endividamento e Impactos Sociais

Este repositório documenta a análise de dados sobre o mercado de apostas esportivas ("bets") no Brasil, estruturada por meio de um pipeline em Python para limpeza e tratamento de dados, exportação para arquivos CSV e visualização interativa em um dashboard executivo no Qlik Sense.

🚀 Visão Geral do Projeto

O objetivo deste projeto é consolidar dados públicos e estudos acadêmicos/governamentais para dimensionar o impacto financeiro, o perfil demográfico dos apostadores e as consequências socioeconômicas (como endividamento e inadimplência) do crescimento das apostas no Brasil.

⚙️ Arquitetura e Pipeline de Dados

Coleta e Tratamento (Python):

Os dados brutos foram extraídos de relatórios de órgãos oficiais e instituições de pesquisa.

Utilizou-se a linguagem Python (com bibliotecas como pandas e numpy) para limpeza, padronização de tipos, tratamento de valores nulos e estruturação das tabelas dimensionais e de fatos.

Exportação (CSV):

Após o processamento, os conjuntos de dados consolidados foram exportados em formato .csv otimizados para importação direta no Qlik Sense.

Visualização (Qlik Sense):

Construção de um painel de Business Intelligence (BI) focado em KPIs estratégicos e segmentação demográfica.

📈 Principais Indicadores (KPIs do Dashboard)

O painel no Qlik Sense exibe os seguintes indicadores chave (referentes ao 1º semestre de 2025):

Apostadores: 17.7 Milhões de brasileiros engajados.

Receita do Mercado: R$ 17.4 Bilhões movimentados.

Bolsa Família: R$ 3.7 Bilhões direcionados para apostas (evidenciando impactos sociais críticos).

Inadimplência: 20% de taxa associada ao endividamento pelo setor.

👥 Perfil dos Apostadores

O dashboard contempla duas análises demográficas centrais:

Faixa Etária (Gráfico de Barras):

Predominância expressiva da faixa de 31 a 40 anos, seguida de perto por jovens de 18 a 25 anos e adultos de 25 a 30 anos. Faixas acima de 50 anos apresentam menor volume, mas relevância para análise de risco.

Gênero (Gráfico de Pizza):

Apostadores Homens: 71.1%

Apostadores Mulheres: 28.9%

📚 Fontes de Dados

Os dados consolidados e transformados originam-se das seguintes instituições:

TCU (Tribunal de Contas da União)

Ministério da Fazenda / Secretaria de Prêmios e Apostas (SPA)

Ministério da Justiça e Segurança Pública (MJSP)

DataSenado

Insper + Stone

Sicredi

IEPS (Instituto de Estudos para Políticas de Saúde)

Banco Central do Brasil

🛠️ Como Utilizar

Scripts Python: Os códigos de extração, tratamento e transformação estão localizados na pasta de scripts (src/ ou diretório raiz).

Dados CSV: Os arquivos tratados prontos para carga estão na pasta data/.

Qlik Sense: Importe os arquivos CSV para o aplicativo Qlik Sense correspondente (Bets-Brasil.qvf ou utilize a conexão de dados baseada nos CSVs).

Desenvolvido como ferramenta de análise de impacto socioeconômico.
