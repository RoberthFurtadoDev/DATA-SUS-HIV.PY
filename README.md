# Projeto de Análise de Casos de AIDS no Maranhão (2018-2023)
# 📌 Visão Geral
Este projeto apresenta um dashboard interativo que analisa os casos de AIDS no estado do Maranhão entre os anos de 2018 e 2023. Desenvolvido como parte da disciplina de Lógica e Matemática Discreta, o projeto utiliza dados públicos do DATASUS para fornecer insights visuais sobre a evolução da doença no período.

# ✨ Funcionalidades
# Visualizações interativas com Plotly.js:

- Gráfico de linha da evolução por sexo

- Gráfico de barras horizontais por faixa etária

- Gráfico de barras empilhadas por ano e faixa etária

- Gráfico de linhas múltiplas por faixa etária

# Design responsivo que se adapta a diferentes tamanhos de tela

# Sidebar informativa com:

- Identificação do projeto

- Informações acadêmicas

- Equipe de desenvolvimento

# 🛠️ Tecnologias Utilizadas
# Backend (Processamento de Dados)
- Python com as seguintes bibliotecas:

- Pandas para manipulação e análise de dados

- Plotly para geração inicial dos gráficos

- Streamlit para prototipagem inicial do dashboard

# Fontes de Dados
DATASUS/TABNET (Sistema de Informação de Agravos de Notificação)

# 🔄 Fluxo de Processamento
Extração: Dados brutos extraídos do DATASUS em formato CSV

# Transformação (Python):

- python
- Copy
- import pandas as pd

# Carregar e limpar dados
- dados = pd.read_csv('casos_aids_ma.csv')
- dados = dados.dropna()
- dados = dados[dados['ano'].between(2018, 2023)]

# Processar para visualização
dados_por_sexo = dados.groupby(['ano', 'sexo']).size().unstack()
dados_por_idade = dados.groupby('faixa_etaria').size()
Visualização: Dados processados são integrados ao dashboard web

# 📊 Estrutura dos Dados
# Os dados analisados incluem:

- Número de casos por ano (2018-2023)

- Distribuição por sexo (masculino/feminino)

- Casos por faixa etária (12 categorias)

- Evolução temporal por faixa etária

# 🚀 Como Utilizar
- Para visualização:
- Clone o repositório:

bash
Copy
git clone https://github.com/seu-usuario/aids-maranhao.git
Abra o arquivo index.html em qualquer navegador moderno.

# Para reprocessamento dos dados:
# Instale as dependências Python:

bash
Copy
pip install pandas plotly streamlit
Execute o script de processamento:

bash
Copy
python processamento_dados.py
# 👥 Equipe
Livius Penha

Roberth Furtado

Gabriel

Eliseu

# Orientador: Prof. Leonardo Henrique Silva Lago

# 📄 Licença
Este projeto utiliza dados públicos do DATASUS e está disponível para fins educacionais. Consulte as políticas de uso de dados do Ministério da Saúde para aplicações profissionais.# DATA-SUS-HIV


# DATA-SUS-HIV.PY
