import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title="AIDS no Maranhão ", layout="wide")
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #004080;  
    }
    [data-testid="stSidebar"] * {
        color: white !important;   
    }
    </style>
""", unsafe_allow_html=True)
echo "#DATA-SUS-HIV.PY" >> README.md

with st.sidebar:
    st.image("logo_datasus.png", width=250)
    st.header("UF: Maranhão")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/45/Bandeira_do_Maranh%C3%A3o.svg",
             width=200)
    st.markdown("---")

    st.markdown("""
    <div style='font-size:18px;'>
        <b>Disciplina:</b> Lógica e Matemática Discreta<br>  
        <br><b>Docente:</b> Leonardo Henrique Silva Lago
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style='font-size:18px;'>
        <b>Discentes:</b><br>
        • Livius Penha<br>
        • Roberth Furtado<br>
        • Gabriel<br>
        • Eliseu
    </div>
    """, unsafe_allow_html=True)


df = pd.read_csv("dados.csv", sep=",")
df = df[df["Ano Notificação"] != "TOTAL"]
df["Ano Notificação"] = df["Ano Notificação"].astype(int)

faixas = ['< 1 ano', '1-4', '5-9', '10-14', '15-19', '20-29', '30-39',
          '50-59', '60-69', '70-79', '80 e mais']

df_sx = pd.read_csv("dados_sx.csv")
df_sx = df_sx[df_sx["Sexo"] != "TOTAL"]

df_sx_long = pd.melt(df_sx, id_vars=["Sexo"], value_vars=["2018", "2019", "2020", "2021", "2022", "2023"],
                     var_name="Ano", value_name="Casos")
df_sx_long["Ano"] = df_sx_long["Ano"].astype(int)


st.markdown("<h1 style='text-align: center; color: #004080;' >Casos de AIDS: De 2018 a 2023</h1>",
            unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: #004080;' >1. Introdução</h2>",
            unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A AIDS (Síndrome da Imunodeficiência Adquirida) continua sendo um dos maiores desafios de saúde pública no Brasil. 
Embora haja avanços significativos na prevenção e no tratamento, a incidência da doença ainda exige atenção constante dos gestores públicos e da sociedade.
Este relatório tem como foco os casos notificados de AIDS no estado do Maranhão, entre os anos de 2018 e 2023, com o objetivo de analisar padrões de ocorrência por ano e faixa etária. 
A escolha do Maranhão justifica-se por sua importância estratégica na Região Nordeste, além de ser um estado com desafios históricos em relação à cobertura de saúde e vigilância epidemiológica.
</p>""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: left; color: #004080;' >2. Metodologia</h2>",
            unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Os dados utilizados neste dashboard foram coletados na plataforma DATASUS, por meio do sistema TABNET/SINAN, que disponibiliza informações públicas sobre doenças e agravos de notificação em todo o território brasileiro.
Foi realizado um recorte específico para o estado do Maranhão, abrangendo o período de 2018 a 2023. Esses dados foram exportados em formato .csv e processados com a linguagem Python, utilizando as bibliotecas:
    <ul style='font-size: 20px; margin-left: 40px;'>
        <li>Pandas para manipulação dos dados;</li>
        <li>Plotly.express para construção dos gráficos interativos;</li>
        <li>Streamlit para desenvolvimento do dashboard apresentado;</li>
    </ul>
</p>""", unsafe_allow_html=True)


st.markdown("<h2 style='text-align: left; color: #004080;' >3. Dashboards apresentados</h2>",
            unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Com base nos dados tratados, foram gerados quatro gráficos, que compõem os dashboards abaixo:
</p>
<p style='font-size: 20px;'>
1. Gráfico de linha que mostra a distribuição de casos por ano com relação ao sexo.<br>
2. Gráfico de barras com os grupos etários mais afetados.<br> 
3. Gráfico de barras empilhadas que mostra como a incidência varia ao longo do tempo.<br>
4. Gráfico de linha que permite observar tendências por grupo etário.<br>
</p>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    fig1 = px.line(df_sx_long, x="Ano", y="Casos", color="Sexo",
                   title="1.Evolução de Casos de AIDS por Sexo (2018–2023)", markers=True)
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    df_total = pd.read_csv("dados.csv")
    casos_por_faixa = df_total[df_total["Ano Notificação"]
                               == "TOTAL"][faixas].T.reset_index()
    casos_por_faixa.columns = ["Faixa Etaria", "Casos"]

    fig2 = px.bar(casos_por_faixa, x="Casos", y="Faixa Etaria", orientation='h',
                  title="2.Distribuição total por faixa etária (2018-2023)")
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    df_long = pd.melt(df, id_vars=["Ano Notificação"], value_vars=faixas,
                      var_name="Faixa Etaria", value_name="Casos")
    fig3 = px.bar(df_long, x="Ano Notificação", y="Casos", color="Faixa Etaria",
                  title="3.Casos por faixa etária ao longo dos anos", barmode="stack")
    st.plotly_chart(fig3, use_container_width=True)
with col4:
    df_linhas = df[["Ano Notificação"] + faixas]
    df_long_line = pd.melt(df_linhas, id_vars="Ano Notificação", value_vars=faixas,
                           var_name="Faixa etaria", value_name="Casos")

    df_long_line["Ano Notificação"] = df_long_line["Ano Notificação"].astype(
        int)

    fig4 = px.line(df_long_line, x="Ano Notificação", y="Casos", color="Faixa etaria",
                   title="4.Evolução por faixa etária", markers=True)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("<h2 style='text-align: left; color: #004080;' >4. Conclusão</h2>",
            unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A análise dos dados de AIDS no Maranhão entre 2018 e 2023 revelou que os casos concentram-se principalmente nas faixas etárias entre 20 e 39 anos, predominantemente no sexo masculino, o que reforça a importância de campanhas direcionadas ao público jovem e adulto.
Além disso, observou-se uma redução no número total de casos nos últimos anos, embora ainda existam variações significativas por grupo etário.
O uso do Python e das bibliotecas modernas de visualização foi essencial para organizar, analisar e apresentar os dados de forma clara e acessível, contribuindo para uma tomada de decisão mais assertiva em saúde pública.<br>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Este dashboard pode ser facilmente adaptado para análises de outros estados ou doenças notificáveis, promovendo a democratização dos dados e a ampliação do conhecimento baseado em evidências.<br>
</p>""", unsafe_allow_html=True)

st.markdown("---")
st.caption(
    "Fonte: DATASUS/TabNet • Desenvolvido por Livius, Roberth, Elisei, Gabriel ©")
